from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

from .client import get_client

model_client = get_client()

query_agent = AssistantAgent(
    name="query_agent",
    model_client=model_client,
    system_message="""
    You are a Github repository search query generator assistant. Based on the user's prompt, you will
    generate an appropriate query to search for using the Github API. Make sure the query will only return 100
    repositories by default, this will be changed if the user specifies a different number.
    Example:
    user: Give me 10 most starred repositories about machine learning with language of Python.
    assistant: "language:python topic:machine-learning stars:>10000 sort:stars-desc"
    """,
)