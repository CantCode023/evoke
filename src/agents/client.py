from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
load_dotenv()

def get_client():
    model_client = OpenAIChatCompletionClient(
        model="gemini-2.0-flash",
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
    
global_client = get_client()