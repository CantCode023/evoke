async def github_repo_fetch_contents(repo_url: str):
    import requests
    import re
    import tarfile, io
    import os

    NON_TEXT_EXTENSIONS = {
        ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp",
        ".mp4", ".avi", ".mov", ".wmv", ".flv", ".mpeg", ".mpg", ".mkv",
        ".mp3", ".wav", ".ogg", ".flac", ".aac", ".wma",
        ".exe", ".dll", ".bin", ".dat", ".so", ".o", ".obj", ".lib", ".a", ".dylib",
        ".zip", ".tar", ".gz", ".tar.gz", ".rar", ".7z", ".xz", ".bz2", ".gzip",
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp",
        ".ttf", ".otf", ".woff", ".woff2", ".eot",
        ".ico", ".svg",
        ".db", ".sqlite", ".mdb", ".accdb",
        ".class", ".jar", ".pyc", ".pyd", ".egg"
    }

    match = re.search(r"github\.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        return "Error: Invalid GitHub repository URL."

    owner, repo_name = match.groups()
    url = f"https://api.github.com/repos/{owner}/{repo_name}/tarball"
    file = requests.get(url)
    
    if file.status_code == 200:
        tar = tarfile.open(fileobj=io.BytesIO(file.content))
        contents = []
        for member in tar.getmembers():
            if member.isfile():
                filename = member.name
                
                _, ext = os.path.splitext(filename)
                if ext.lower() in NON_TEXT_EXTENSIONS:
                    continue

                contents.append({
                    "path": filename,
                    "content": tar.extractfile(member).read().decode('utf-8', errors="replace")
                })
                
        return contents
    else:
        return f"Error {file.status_code}: Failed to fetch file contents.\n{file.content}"