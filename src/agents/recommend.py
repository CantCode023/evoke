from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

from .client import get_client
from src.tools.repo import github_repo_search

recommend_agent = AssistantAgent(
    name="recommend_agent",
    model_client=get_client(),
    system_message="""
    You are a project recommendation agent. 
    Given the list of github repositories, choose the repositories that best match the user's prompt.
    Display only the URLs of chosen repositories.
    """
)
