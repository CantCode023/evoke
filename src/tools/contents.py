from typing import List, Dict, Optional
from dataclasses import dataclass
import requests
import tarfile
import re
import io
import os

@dataclass
class RepoContent:
    path: str
    content: str

class GithubContentFetcher:
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

    @staticmethod
    def _parse_repo_url(repo_url: str) -> Optional[tuple[str, str]]:
        match = re.search(r"github\.com/([^/]+)/([^/]+)", repo_url)
        return match.groups() if match else None
    
    @classmethod
    def _is_text_file(cls, filename: str) -> bool:
        _, ext = os.path.splitext(filename)
        return ext.lower() not in cls.NON_TEXT_EXTENSIONS
    
    @classmethod
    def _process_tar_member(cls, tar: tarfile.TarFile, member: tarfile.TarInfo) -> Optional[RepoContent]:
        if not member.isfile() or not cls._is_text_file(member.name):
            return None
        
        try:
            content = tar.extractfile(member).read().decode('utf-8', errors="replace")
            return RepoContent(path=member.name, content=content)
        except Exception:
            return None

async def github_repo_fetch_contents(repo_url: str) -> List[Dict[str, str]] | str:
    repo_info = GithubContentFetcher._parse_repo_url(repo_url)
    if not repo_info:
        return "Error: Invalid GitHub repository URL."
    
    owner, repo_name = repo_info
    url = f"https://api.github.com/repos/{owner}/{repo_name}/tarball"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        tar = tarfile.open(fileobj=io.BytesIO(response.content))
        contents = []
        
        for member in tar.getmembers():
            content = GithubContentFetcher._process_tar_member(tar, member)
            if content:
                contents.append({
                    "path": content.path,
                    "content": content.content
                })
        
        return contents
    except Exception as e:
        return f"Error: Failed to fetch file contents.\n{str(e)}"