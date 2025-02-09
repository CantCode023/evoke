from autogen_agentchat.agents import UserProxyAgent

user_proxy = UserProxyAgent("user_proxy", input_func=lambda _: input("[:] "))