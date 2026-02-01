import json
from pathlib import Path
from app.config import settings

class StateStore:
    def __init__(self):
        self.path = Path(settings.STATE_FILE)
        self.path.parent.mkdir(exist_ok=True)
        self.state = self._load()

    def _load(self):
        if self.path.exists():
            return json.loads(self.path.read_text())
        return {}

    def save(self):
        self.path.write_text(json.dumps(self.state, indent=2))

    def get_hash(self, article_id):
        return self.state.get(str(article_id))

    def set_hash(self, article_id, hash_value):
        self.state[str(article_id)] = hash_value