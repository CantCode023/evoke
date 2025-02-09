from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console

from src.agents.query import query_agent
from src.agents.recommend import recommend_agent
from src.agents.user import user_proxy
from src.agents.report import report_agent

class Evoke:
    def __init__(self):
        text_termination = TextMentionTermination("TERMINATE")
        
        self.team = RoundRobinGroupChat(
            [query_agent, recommend_agent, user_proxy, report_agent],
            termination_condition=text_termination,
            max_turns=4
        )
    
    async def ask(self, task_message: str):
        await Console(self.team.run_stream(task=task_message))