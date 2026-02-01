from bs4 import BeautifulSoup
from markdownify import markdownify as md

def clean_and_convert(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["nav", "footer", "aside", "script", "style"]):
        tag.decompose()

    return md(str(soup))