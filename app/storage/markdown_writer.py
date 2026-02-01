from pathlib import Path
from slugify import slugify
from app.config import settings

class MarkdownWriter:
    def __init__(self):
        self.base = Path(settings.OUTPUT_DIR)
        self.base.mkdir(parents=True, exist_ok=True)

    def write(self, title: str, content: str):
        slug = slugify(title)
        path = self.base / f"{slug}.md"
        path.write_text(content, encoding="utf-8")
        return path