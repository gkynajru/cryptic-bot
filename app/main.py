from app.logging import setup_logging
from app.scraper.scraper import ArticleScraper
from app.storage.state_store import StateStore
from app.storage.markdown_writer import MarkdownWriter
from app.utils.hashing import hash_text
from app.openai.vector_store import get_or_create_vector_store
from app.openai.uploader import upload_files
from app.config import settings
import logging

def main():
    setup_logging()
    log = logging.getLogger(__name__)

    scraper = ArticleScraper()
    state = StateStore()
    writer = MarkdownWriter()

    articles = scraper.scrape_all()
    new, updated, skipped = 0, 0, 0
    written_files = []

    for a in articles:
        md = scraper.to_markdown(a)
        h = hash_text(md)

        old = state.get_hash(a["id"])
        if old == h:
            skipped += 1
            continue

        path = writer.write(a["title"], md)
        state.set_hash(a["id"], h)
        written_files.append(path)

        if old is None:
            new += 1
        else:
            updated += 1

    state.save()

    if written_files:
        vs = get_or_create_vector_store(settings.VECTOR_STORE_NAME)
        upload_files(vs.id, written_files)

    log.info(f"Added: {new}, Updated: {updated}, Skipped: {skipped}")

if __name__ == "__main__":
    main()