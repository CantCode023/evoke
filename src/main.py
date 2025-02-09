from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken

from src.agents.query import query_agent
from src.agents.context import add_context
from src.agents.recommend import recommend_agent

from src.tools.repo import github_repo_search
from src.tools.readme import github_repo_fetch_readme

class Evoke:
    def __init__(self):
        text_termination = TextMentionTermination("TERMINATE")
        
        context_agent = add_context(github_repo_search)
        readme_context_agent = add_context(
            github_repo_fetch_readme,
            system_message="From the list of repositories URLs, fetch the README.md file for each one and return the content."
        )
        
        self.team = RoundRobinGroupChat(
            [query_agent, context_agent, recommend_agent, readme_context_agent],
            termination_condition=text_termination,
            max_turns=4
        )
    
    async def ask(self, task_message: str):
        await Console(self.team.run_stream(task="Recommend 10 Python projects about machine learning and cybersecurity."))