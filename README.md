
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
* Uploads only deltas
* Logs added, updated, and skipped counts

Note: I don't know how to get the link of daily job logs, so I put the screenshot of the logs here:

📸 Activities: ![Screenshot](https://github.com/gkynajru/cryptic-bot/blob/main/screenshot/Logs.png)

📸 Details: ![Screenshot](https://github.com/gkynajru/cryptic-bot/blob/main/screenshot/log_detail.png)