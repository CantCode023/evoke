from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console

from src.agents.query import query_agent
from src.agents.recommend import recommend_agent
from src.agents.user import user_proxy
from src.agents.report import report_agent
from src.agents.client import get_client

class Evoke:
    def __init__(self):
        self.agent_order = [query_agent, recommend_agent, user_proxy, report_agent]
        self.current_index = 0
        
        def selector_func(message):
            if message[-1].content == "REGENERATE" and message[-1].source == "user_proxy":
                self.current_index = 2
                return "recommend_agent"
            elif "REPORT_BACK" in message[-1].content and message[-1].source == "report_agent":
                self.current_index = 3
                return "user_proxy"
            
            next_agent = self.agent_order[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.agent_order)
            
            return next_agent.name
        
        self.team = SelectorGroupChat(
            self.agent_order,
            model_client=get_client(),
            termination_condition=TextMentionTermination("TERMINATE"),
            selector_func=selector_func
        )
    
    async def ask(self, task_message: str):
        await Console(self.team.run_stream(task=task_message))