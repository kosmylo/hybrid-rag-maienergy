from retrievers.hybrid_retriever import hybrid_search

query = "renewable energy Austria"
results = hybrid_search(query, top_k_per_source=3, final_top_k=10)

print("\nTop Hybrid RAG Results:\n")
for idx, res in enumerate(results, 1):
    source_info = getattr(res, "_source", getattr(res, "entity", getattr(res, "metadata", {})))
    print(f"Result {idx}: {source_info}\n{'-'*80}")