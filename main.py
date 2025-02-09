from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken

from src.agents.query import query_agent
from src.agents.context import add_context
from src.agents.recommend import recommend_agent

from src.tools.repo import github_repo_search

text_termination = TextMentionTermination("TERMINATE")

context_agent = add_context(github_repo_search)

team = RoundRobinGroupChat(
    [query_agent, context_agent, recommend_agent],
    termination_condition=text_termination,
    max_turns=3
)

async def main():
    await Console(team.run_stream(task="Recommend 10 Python projects about machine learning and cybersecurity."))
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())