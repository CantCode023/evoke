from autogen_agentchat.agents import AssistantAgent

from .client import get_client

query_agent = AssistantAgent(
    name="query_agent",
    model_client=get_client(),
    system_message="""
    You are a Github repository search query generator.
    Your task is to generate a Github search query based on the user's prompt.
    Example:
    user: Give me 10 most starred repositories about machine learning with language of Python.
    assistant: "language:python topic:machine-learning stars:>10000 sort:stars-desc"
    """,
)