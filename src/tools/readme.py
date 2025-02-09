import requests
import re

async def github_repo_fetch_readme(repo_url: str):
    match = re.search(r"github\.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        return "Error: Invalid GitHub repository URL."

    owner, repo_name = match.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/"
    headers = {
        "Accept": "application/vnd.github+json",
    }
    
    response = requests.get(api_url, headers=headers)
    data = response.json()
    
    for item in data:
        if item["type"] == "file" and item["name"] == "README.md":
            download_url = item["download_url"]
            readme_file = requests.get(download_url)
            if readme_file.status_code == 200:
                return readme_file.text
            else:
                print(f"Error fetching README.md content: {readme_file.status_code}")
                break
        else:
            print(f"Error fetching repo contents: {response.status_code}")
            return {}