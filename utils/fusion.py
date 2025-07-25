import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def reciprocal_rank_fusion(results, top_k=10):
    fused_scores = {}
    for source_type in set([res["source"] for res in results]):
        source_results = [res for res in results if res["source"] == source_type]
        source_results.sort(key=lambda x: x["score"] or 0, reverse=True)
        logger.info(f"Fusing {len(source_results)} results from source '{source_type}'")
        for rank, res in enumerate(source_results, 1):
            doc_id = f"{res['source']}_{res['database']}_{rank}"
            score = 1 / (rank + 1)
            if doc_id in fused_scores:
                fused_scores[doc_id]["fused_score"] += score
            else:
                fused_scores[doc_id] = {"result": res, "fused_score": score}

    # Sort by fused score
    sorted_results = sorted(fused_scores.values(), key=lambda x: x["fused_score"], reverse=True)
    logger.info(f"Returning top {top_k} fused results after rank fusion")
    return [item["result"] for item in sorted_results[:top_k]]
    