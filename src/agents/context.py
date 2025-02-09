from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

from .client import get_client

def add_context(*tool):
    context_agent = AssistantAgent(
        name="context_agent",
        model_client=get_client(),
        tools=[*tool],
        system_message="""Use the tool given and return the results."""
    )
    
    return context_agent