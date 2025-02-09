async def github_repo_fetch_contents(repo_url: str):
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
    results = []
    
    for item in data:
        download_url = item["download_url"]
        file = requests.get(download_url)
        if file.status_code == 200:
            results.append({
                "name": item["name"],
                "content": file.text
            })
            return file.text
        else:
            print(f"Error {response.status_code}: Failed to fetch file contents.\n{data}") 
            return {}