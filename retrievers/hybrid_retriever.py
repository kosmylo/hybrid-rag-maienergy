from retrievers.opensearch_retriever import semantic_search
from retrievers.milvus_retriever import milvus_search
from retrievers.neo4j_retriever import neo4j_search
from utils.fusion import reciprocal_rank_fusion
from config.db_config import OPENSEARCH_INDEX_CONFIG, MILVUS_COLLECTION_CONFIG, NEO4J_NODE_CONFIG

def hybrid_search(query, top_k_per_source=3, final_top_k=10):
    all_results = {}

    # Query all OpenSearch indexes
    for index_name in OPENSEARCH_INDEX_CONFIG.keys():
        os_results = semantic_search(index_name, query, top_k_per_source)
        all_results[f'opensearch_{index_name}'] = os_results

    # Query all Milvus collections
    for collection_name in MILVUS_COLLECTION_CONFIG.keys():
        milvus_results = milvus_search(collection_name, query, top_k_per_source)
        all_results[f'milvus_{collection_name}'] = milvus_results[0]  # Milvus returns nested lists

    # Query all Neo4j nodes
    for category, nodes in NEO4J_NODE_CONFIG.items():
        for node_label, props in nodes.items():
            text_property = "title" if "title" in props else ("name" if "name" in props else props[0])
            index_name = f"{category.lower()}_{node_label.lower()}_index"
            neo4j_results = neo4j_search(index_name, node_label, text_property, query, top_k_per_source)
            all_results[f'neo4j_{category}_{node_label}'] = neo4j_results

    # Aggregate all results
    fused_results = reciprocal_rank_fusion(all_results, top_k=final_top_k)
    return fused_results