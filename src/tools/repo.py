import requests

def github_repo_search(query: str) -> str:
    url = f"https://api.github.com/search/repositories"
    params = {
        "q": query,
    }
    headers = {
        "Accept": "application/vnd.github+json",
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # TODO: Only return needed data (i.e name, description, url)
        return data
    else:
        return f"respond with 'Error {response.status_code}: Failed to search for repositories.\n{response.json()}', finally, respond with TERMINATE"