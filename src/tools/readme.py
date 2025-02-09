async def github_repo_fetch_readme(repo_url: str):
    import requests
    import re

    match = re.search(r"github\.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        return "Error: Invalid GitHub repository URL."

    owner, repo_name = match.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/README.md"
    headers = {
        "Accept": "application/vnd.github+json",
    }
    
    response = requests.get(api_url, headers=headers)
    data = response.json()
    
    download_url = data["download_url"]
    readme_file = requests.get(download_url)
    if readme_file.status_code == 200:
        return readme_file.text
    else:
       print(f"Error {response.status_code}: Failed to fetch README.md file.\n{data}") 
       return {}