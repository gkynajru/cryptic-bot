from app.scraper.zendesk_client import ZendeskClient
from app.scraper.article_cleaner import clean_and_convert

class ArticleScraper:
    def __init__(self):
        self.client = ZendeskClient()

    def scrape_all(self, max_articles=50):
        articles = []
        page = 1

        while len(articles) < max_articles:
            data = self.client.fetch_articles(page)
            articles.extend(data["articles"])
            if not data.get("next_page"):
                break
            page += 1

        return articles[:max_articles]

    def to_markdown(self, article):
        content = clean_and_convert(article["body"])
        return (
            f"# {article['title']}\n\n"
            f"Article URL: {article['html_url']}\n\n"
            f"{content}"
        )