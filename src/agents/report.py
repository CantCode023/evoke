from autogen_agentchat.agents import AssistantAgent

from .client import get_client_for_report
from src.tools.contents import github_repo_fetch_contents

report_agent = AssistantAgent(
    name="report_agent",
    model_client=get_client_for_report(),
    tools=[github_repo_fetch_contents],
    system_message="""
    Using the tool given, fetch the contents of the given repository URL.
    After fetching the repository contents, display details in this format:
        
    # Repository name
    > Short description of the repository
    
    ```
    Estimated day to write: X days
    Difficulty: Easy/Medium/Hard
    Language: X (e.g Python/Java/C++, etc.)
    ```
    
    # 📚 Libraries Used
    ```
    (Give the libraries used in the repository, for example, if the library requests is uesd in example.py, put that library here.)
    e.g 
    requests
    beautifulsoup4
    etc.
    (This can be found in requuirements.txt if available.)
    ```
    
    # ✨ Core Features
    ## (Feature that needs to be implemented e.g proxy pool rotation)
    - How to implement the feature (e.g using python requests library, call a request to ...)
    - (e.g After calling the request, ...)
    - (e.g Finally, ...)
    
    # 📝 Details
    > (Explain what the repository does in detail.)
    
    # 📢 Informations
    - (Important informations about the repository based on the README.md)
    - (Second information)
    - (Third information)
     
    Finally, respond with TERMINATE.
    """,
   reflect_on_tool_use=True 
)