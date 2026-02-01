import requests
from app.config import settings

class ZendeskClient:
    def fetch_articles(self, page: int = 1):
        url = f"{settings.ZENDESK_BASE_URL}/api/v2/help_center/en-us/articles.json"
        resp = requests.get(url, params={"page": page})
        resp.raise_for_status()
        return resp.json()