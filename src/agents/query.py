from autogen_agentchat.agents import AssistantAgent

from .client import get_client

query_agent = AssistantAgent(
    name="query_agent",
    model_client=get_client(),
    system_message="""
    You are a Github repository search query generator assistant.
    Your task is to generate a query based on the user's prompt to use in the Github search repository API.
    The query generated must be syntactically correct following the Github search repository API syntax. https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories
    
    Example:
    user: Python project about machine learning that'd take less than a week to complete.
    assistant: "language:python topic:machine-learning size:<=1000"
    """,
)