from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

from .client import get_client

def generate_hash() -> str:
    import string, random
    return "".join(random.choices(string.ascii_lowercase, k=12))

def add_context(*tool, system_message:str|None=None) -> AssistantAgent:
    hash_name = generate_hash() + "_context_agent"
    context_agent = AssistantAgent(
        name=hash_name,
        model_client=get_client(),
        tools=[*tool],
        system_message="""Use the tool given and return the results.""" if system_message is None else system_message,
    )
    
    return context_agent