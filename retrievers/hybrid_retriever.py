from retrievers.opensearch_retriever import hybrid_search as opensearch_search
from retrievers.milvus_retriever import milvus_search
from retrievers.neo4j_retriever import neo4j_search
from config.db_config import OPENSEARCH_INDEX_CONFIG, MILVUS_COLLECTION_CONFIG, NEO4J_NODE_CONFIG
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def unified_hybrid_search(query, top_k_per_source=3):
    results = []

    # OpenSearch
    logger.info(f"Starting OpenSearch retrieval for query: '{query}'")
    for index in OPENSEARCH_INDEX_CONFIG:
        try:
            opensearch_results = opensearch_search(index, query, top_k=top_k_per_source)
            logger.info(f"OpenSearch '{index}' returned {len(opensearch_results)} results")
            for res in opensearch_results:
                results.append({
                    "source": "opensearch",
                    "database": index,
                    "content": res['source'],
                    "score": res['score']
                })
        except Exception as e:
            logger.error(f"OpenSearch retrieval error on '{index}': {e}")

    # Milvus
    logger.info(f"Starting Milvus retrieval for query: '{query}'")
    for collection in MILVUS_COLLECTION_CONFIG:
        try:
            milvus_results = milvus_search(collection, query, top_k=top_k_per_source)
            retrieved_count = len(milvus_results[0]) if milvus_results else 0
            logger.info(f"Milvus '{collection}' returned {retrieved_count} results")
            for hit in milvus_results[0]:
                results.append({
                    "source": "milvus",
                    "database": collection,
                    "content": hit.entity,
                    "score": 1 - hit.distance
                })
        except Exception as e:
            logger.error(f"Milvus retrieval error on '{collection}': {e}")

    # Neo4j
    logger.info(f"Starting Neo4j retrieval for query: '{query}'")
    for category, nodes in NEO4J_NODE_CONFIG.items():
        for node_label, props in nodes.items():
            index_name = f"{category.lower()}_{node_label.lower()}_index"
            text_property = "title" if "title" in props else ("name" if "name" in props else props[0])
            try:
                neo4j_results = neo4j_search(index_name, node_label, text_property, query, top_k=top_k_per_source)
                logger.info(f"Neo4j '{category}.{node_label}' returned {len(neo4j_results)} results")
                for res, score in neo4j_results:
                    results.append({
                        "source": "neo4j",
                        "database": f"{category}.{node_label}",
                        "content": {
                            text_property: res.page_content,
                            **res.metadata
                        },
                        "score": score  # similarity score provided by Neo4j
                    })
            except Exception as e:
                logger.error(f"Neo4j Error on {category}.{node_label}: {e}")

    logger.info(f"Total combined results before fusion: {len(results)}")
    return results