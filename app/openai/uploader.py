from openai import OpenAI

client = OpenAI()

def upload_files(vector_store_id: str, paths: list):
    file_ids = []

    for p in paths:
        uploaded = client.files.create(
            file=open(p, "rb"),
            purpose="assistants"
        )
        file_ids.append(uploaded.id)

    client.vector_stores.files.batch_create(
        vector_store_id=vector_store_id,
        file_ids=file_ids
    )