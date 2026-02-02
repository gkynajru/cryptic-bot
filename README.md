
This project implements a minimal OptiBot-style backend that scrapes OptiSigns
support articles, normalizes them into Markdown, and loads them into an OpenAI
Vector Store for retrieval-based Q&A.

---

## Setup

### Requirements
- Python 3.11+
- Docker
- OpenAI API key

Create a `.env` file:
```bash
OPENAI_API_KEY=your_key_here
````

---

## Run Locally

```bash
pip install -r requirements.txt
python -m app.main
```

The job:

* Scrapes OptiSigns Zendesk articles
* Converts them to clean Markdown
* Detects new/updated content via hashing
* Uploads only deltas to the OpenAI Vector Store

---

## Run with Docker

```bash
docker build -t cryptic-bot .
docker run -e OPENAI_API_KEY=your_key_here cryptic-bot
```

The container runs once and exits with code 0.

---

## Scraping & Normalization

* Source: `support.optisigns.com` (Zendesk Help Center API)
* Articles scraped: 50
* Navigation, ads, and scripts are removed
* Markdown preserves headings, lists, code blocks, and relative links
* Each file includes an `Article URL:` line for citation

---

## Vector Store & Chunking Strategy

* Markdown files are uploaded programmatically via OpenAI API
* Files are attached using `file_batches.create_and_poll`
* Chunking is handled by OpenAI’s default semantic chunker
* Each article is chunked by section, preserving context while keeping retrieval precise

---

## Assistant Sanity Check

A one-time Assistant was created via the OpenAI Playground UI to verify retrieval.

**Test question:**

> How do I add a YouTube video?

The Assistant correctly answers using the uploaded documents and cites the relevant
OptiSigns support article.

📸 Screenshot: ![Screenshot](https://github.com/gkynajru/cryptic-bot/blob/main/screenshot/playground_youtube_answer.png)

---

## Daily Job

The scraper-uploader is designed to run as a daily job:

* Re-scrapes articles
* Detects new or updated content via SHA-256 hashing
* Uploads only deltas
* Logs added, updated, and skipped counts