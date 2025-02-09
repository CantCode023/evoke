async def github_repo_search(query: str) -> str | dict[str, str]:
    import requests

    url = f"https://api.github.com/search/repositories"
    params = {
        "q": query,
    }
    headers = {
        "Accept": "application/vnd.github+json",
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()["items"]
        if len(data) > 100:
            data = data[:100]
        
        projects = {}
        for project in data:
            projects[project["full_name"]] = {}
            current_project = projects[project["full_name"]]
            
            current_project["title"] = project["full_name"]
            current_project["description"] = project["description"]
            current_project["url"] = project["html_url"]
            current_project["topics"] = project["topics"]
            
        return projects
    else:
        return f"respond with 'Error {response.status_code}: Failed to search for repositories.\n{response.json()}', finally, respond with TERMINATE"