from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import SelectorGroupChat

from src.agents.query import query_agent
from src.agents.recommend import recommend_agent
from src.agents.user import user_proxy
from src.agents.report import report_agent
from src.agents.client import get_client

class Evoke:
    def __init__(self):
        text_termination = TextMentionTermination("TERMINATE")
        
        self.agent_order = [query_agent, recommend_agent, user_proxy, report_agent]
        self.current_index = 0
        
        def selector_func(message):
            if message[-1].content == "REGENERATE" and message[-1].source == "user_proxy":
                self.current_index = 2
                return "recommend_agent"
            
            next_agent = self.agent_order[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.agent_order)
            
            return next_agent.name
        
        self.team = SelectorGroupChat(
            participants=self.agent_order,
            model_client=get_client(),
            termination_condition=text_termination,
            selector_func=selector_func
        )
    
    async def ask(self, task_message: str):
        result = await self.team.run(task=task_message)
        return result