from app.openai.client import client

def upload_files(vector_store_id: str, paths: list):
    file_ids = []
    for p in paths:
        f = client.files.create(
            file=open(p, "rb"),
            purpose="assistants"
        )
        file_ids.append(f.id)

    client.vector_stores.file_batches.create(
        vector_store_id=vector_store_id,
        file_ids=file_ids
    )