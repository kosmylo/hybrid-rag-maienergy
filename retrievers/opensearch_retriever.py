import os
from opensearchpy import OpenSearch
from dotenv import load_dotenv
from embeddings.text_embeddings import embed_text
from config.db_config import OPENSEARCH_INDEX_CONFIG

load_dotenv()

OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST")

client = OpenSearch(hosts=[OPENSEARCH_HOST])

def semantic_search(index_name, query, top_k=5):
    query_vector = embed_text(query)
    search_body = {
        "size": top_k,
        "query": {
            "knn": {
                "embedding": {
                    "vector": query_vector,
                    "k": top_k
                }
            }
        },
        "_source": OPENSEARCH_INDEX_CONFIG.get(index_name, [])
    }
    response = client.search(index=index_name, body=search_body)
    return response['hits']['hits']

def keyword_search(index_name, query, top_k=5):
    search_body = {
        "size": top_k,
        "query": {
            "match": {
                "text_chunk": query
            }
        },
        "_source": OPENSEARCH_INDEX_CONFIG.get(index_name, [])
    }
    response = client.search(index=index_name, body=search_body)
    return response['hits']['hits']

def normalize_scores(results):

    if not results:  # Handle empty results explicitly
        return []
    
    scores = [hit["_score"] for hit in results]
    min_score, max_score = min(scores), max(scores)
    range_score = max_score - min_score if max_score != min_score else 1.0
    normalized = [
        {
            "source": hit["_source"],
            "score": (hit["_score"] - min_score) / range_score
        }
        for hit in results
    ]
    return normalized

def hybrid_search(index_name, query, top_k=5, semantic_weight=0.7, keyword_weight=0.3):
    semantic_results = semantic_search(index_name, query, top_k=top_k*2)
    keyword_results = keyword_search(index_name, query, top_k=top_k*2)
    
    # Normalize scores 
    semantic_normalized = normalize_scores(semantic_results)
    keyword_normalized = normalize_scores(keyword_results)

    if not semantic_normalized and not keyword_normalized:
        return []

    results_dict = {}

    for res in semantic_normalized:
        doc_id = res["source"].get("url", "") + str(res["source"].get("chunk_id", ""))
        score = res["score"] * semantic_weight
        results_dict[doc_id] = {"source": res["source"], "score": score}

    for res in keyword_normalized:
        doc_id = res["source"].get("url", "") + str(res["source"].get("chunk_id", ""))
        score = res["score"] * keyword_weight
        if doc_id in results_dict:
            results_dict[doc_id]["score"] += score
        else:
            results_dict[doc_id] = {"source": res["source"], "score": score}

    combined_results = sorted(results_dict.values(), key=lambda x: x["score"], reverse=True)
    return combined_results[:top_k]