from pymilvus import connections, Collection
import os
from dotenv import load_dotenv
from embeddings.multimodal_embeddings import embed_text_clip

load_dotenv()
connections.connect(host=os.getenv("MILVUS_HOST"), port=os.getenv("MILVUS_PORT"))

def milvus_search(collection_name, query, top_k=5):
    collection = Collection(collection_name)
    collection.load()
    vector = embed_text_clip(query)
    params = {"metric_type": "COSINE"}
    return collection.search([vector], "embedding", params, top_k)
