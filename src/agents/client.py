from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
load_dotenv()

def get_client():
    model_client = OpenAIChatCompletionClient(
        model="google/gemini-2.0-flash-exp:free",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": "unknown"
        }
    )
    
    return model_client
    
def get_client_for_report():
    model_client = OpenAIChatCompletionClient(
        model="google/gemini-2.0-flash-exp:free",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": "unknown"
        }
    )
    
    return model_client