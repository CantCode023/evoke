from typing import List, Dict, Union, Optional
import requests
from dataclasses import dataclass
from urllib.parse import urlencode

@dataclass
class Repository:
    title: str
    description: Optional[str]
    url: str
    topics: List[str]

class GithubRepoSearcher:
    BASE_URL = "https://api.github.com/search/repositories"
    MAX_RESULTS = 100
    
    def __init__(self):
        self.headers = {
            "Accept": "application/vnd.github+json"
        }
    
    def _encode_url(self, query: str) -> str:
        params = {"q": query}
        return f"{self.BASE_URL}?{urlencode(params)}"
    
    def _process_repository(self, repo_data: Dict) -> Repository:
        return Repository(
            title=repo_data["full_name"],
            description=repo_data.get("description"),
            url=repo_data["html_url"],
            topics=repo_data.get("topics", [])
        )
    
    def _process_response(self, data: Dict) -> Dict[str, Repository]:
        repositories = {}
        for repo in data["items"][:self.MAX_RESULTS]:
            repository = self._process_repository(repo)
            repositories[repository.title] = repository.__dict__
        return repositories

async def github_repo_search(query: str) -> Union[str, Dict[str, Dict[str, Union[str, Optional[str], List[str]]]]]:
    try:
        searcher = GithubRepoSearcher()
        response = requests.get(
            searcher._encode_url(query),
            headers=searcher.headers
        )
        response.raise_for_status()
        
        return searcher._process_response(response.json())
        
    except requests.exceptions.RequestException as e:
        error_msg = f"Error {e.response.status_code if hasattr(e, 'response') else 'Unknown'}"
        error_details = e.response.json() if hasattr(e, 'response') else str(e)
        return f"respond with '{error_msg}: Failed to search for repositories.\n{error_details}', finally, respond with TERMINATE"