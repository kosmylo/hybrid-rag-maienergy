def reciprocal_rank_fusion(results_dict, top_k=10):
    fused_scores = {}
    for source, results in results_dict.items():
        for rank, result in enumerate(results):
            doc_id = f"{source}_{getattr(result, '_id', getattr(result, 'id', rank))}"
            score = 1 / (rank + 1)
            fused_scores[doc_id] = (fused_scores.get(doc_id, 0) + score, result)

    sorted_docs = sorted(fused_scores.values(), key=lambda x: x[0], reverse=True)
    return [doc for _, doc in sorted_docs[:top_k]]