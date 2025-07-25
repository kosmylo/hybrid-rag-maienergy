from retrievers.hybrid_retriever import unified_hybrid_search
from utils.fusion import reciprocal_rank_fusion
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def test_hybrid_rag(query, top_k_per_source=3, final_top_k=10):
    logger.info(f"Performing unified hybrid retrieval for query: '{query}'")
    results = unified_hybrid_search(query, top_k_per_source=top_k_per_source)
    logger.info("Performing reciprocal rank fusion")
    fused_results = reciprocal_rank_fusion(results, top_k=final_top_k)

    print(f"\n--- Final Hybrid RAG Results for '{query}' ---\n")
    for idx, res in enumerate(fused_results, 1):
        print(f"Rank {idx}: (Source: {res['source']} - Database: {res['database']})")
        for key, value in res['content'].items():
            print(f"{key.capitalize()}: {value}")
        print(f"Similarity Score: {res['score']:.4f}")
        print("-" * 50)

if __name__ == "__main__":
    query = "renewable energy Austria"
    test_hybrid_rag(query)
