from app.openai.client import get_client

def get_or_create_vector_store(name: str):
    client = get_client()
    stores = client.vector_stores.list()
    for s in stores.data:
        if s.name == name:
            return s
    return client.vector_stores.create(name=name)
