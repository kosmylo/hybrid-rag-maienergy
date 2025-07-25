import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def weighted_rrf(results, top_k=10, source_weights=None):
    if source_weights is None:
        source_weights = {"opensearch": 0.6, "milvus": 0.1, "neo4j": 0.3}

    fused_scores = {}
    for source_type in set(res["source"] for res in results):
        weight = source_weights.get(source_type, 1.0)
        source_results = sorted(
            [res for res in results if res["source"] == source_type],
            key=lambda x: x["score"] or 0, reverse=True
        )
        for rank, res in enumerate(source_results, 1):
            doc_id = f"{res['source']}_{res['database']}_{res['content'].get('id', rank)}"
            score = weight / (rank + 1)
            fused_scores[doc_id] = fused_scores.get(doc_id, {"result": res, "fused_score": 0})
            fused_scores[doc_id]["fused_score"] += score

    sorted_results = sorted(fused_scores.values(), key=lambda x: x["fused_score"], reverse=True)
    return [item["result"] for item in sorted_results[:top_k]]