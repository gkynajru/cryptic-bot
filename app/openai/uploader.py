from app.openai.client import get_client

def upload_files(vector_store_id: str, paths: list):
    client = get_client()

    file_ids = []
    for p in paths:
        uploaded = client.files.create(
            file=open(p, "rb"),
            purpose="assistants"
        )
        file_ids.append(uploaded.id)

    client.vector_stores.file_batches.create_and_poll(
        vector_store_id=vector_store_id,
        file_ids=file_ids
    )
