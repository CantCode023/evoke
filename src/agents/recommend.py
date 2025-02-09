from autogen_agentchat.agents import AssistantAgent

from .client import get_client
from src.tools.repo import github_repo_search

recommend_agent = AssistantAgent(
    name="recommend_agent",
    model_client=get_client(),
    tools=[github_repo_search],
    system_message="""
    You are a project recommendation agent. 
    Use the tool given to find github repositories based on the query given.
    Given the list of github repositories, choose the repositories that best match the user's prompt.
    Make sure to return at least 5 repositories.
    Note that the repositories recommended must not be a repository that works as a package.
    For example, do not recommend "https://github.com/fastapi/fastapi", but instead recommend repositories that uses fastapi to make a unique project.
    Display the URLs of chosen repositories and the description below it.
    If an error occurs, return the error message and then return TERMINATE.
    Example:
    - URL
    > Description
    (newline)
    - URL 2
    > Description 2
    ...
    """,
    reflect_on_tool_use=True
)
