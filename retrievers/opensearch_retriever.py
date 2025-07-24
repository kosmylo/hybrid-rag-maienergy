from opensearchpy import OpenSearch
from dotenv import load_dotenv
import os
from embeddings.text_embeddings import embed_text

load_dotenv()
OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST")

client = OpenSearch(hosts=[OPENSEARCH_HOST])

def semantic_search(index, query, top_k=5):
    vector = embed_text(query)
    body = {"size": top_k, "query": {"knn": {"embedding": {"vector": vector, "k": top_k}}}}
    return client.search(index=index, body=body)["hits"]["hits"]