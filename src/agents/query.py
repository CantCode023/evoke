from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

from .client import get_client

query_agent = AssistantAgent(
    name="query_agent",
    model_client=get_client(),
    system_message="""
    You are a Github repository search query generator. Based on the user's prompt, you'll
    generate a query to search in the Github API. Make sure to not limit the results by user's prompt.
    For example, if the user asks for 10 most starred repos, do not limit the results to 10 repos.
    Example:
    user: Give me 10 most starred repositories about machine learning with language of Python.
    assistant: "language:python topic:machine-learning stars:>10000 sort:stars-desc"
    """,
)