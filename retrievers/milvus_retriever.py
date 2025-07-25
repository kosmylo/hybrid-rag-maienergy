from pymilvus import connections, Collection
import os
from dotenv import load_dotenv
from embeddings.multimodal_embeddings import embed_text_clip
from config.db_config import MILVUS_COLLECTION_CONFIG
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger("Milvus")

MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT")

connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)

def milvus_search(collection_name, query, top_k=5):
    collection = Collection(collection_name)
    collection.load()
    vector = embed_text_clip(query)
    search_params = {"metric_type": "COSINE"}
    output_fields = MILVUS_COLLECTION_CONFIG.get(collection_name, [])
    results = collection.search(
        data=[vector],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=output_fields
    )
    logger.info(f"Milvus results for '{collection_name}': {results}")
    return results
