from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
load_dotenv()

def get_client():
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        base_url="https://generativelanguage.googleapis.com/v1beta/",
        api_key=os.environ["GEMINI_API_KEY"],
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "family": "unknown"
        }
    )
    
    return model_client
    
def get_client_for_report():
    model_client = OpenAIChatCompletionClient(
        model="gemini-2.0-pro-exp-02-05",
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ["GEMINI_API_KEY"],
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "family": "unknown"
        }
    )
    
    return model_client