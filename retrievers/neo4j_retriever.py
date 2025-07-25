import os
from dotenv import load_dotenv
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from embeddings.text_embeddings import text_embedding_model
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger("Neo4j")

NEO4J_URL = os.getenv("NEO4J_URL")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def neo4j_search(index_name, node_label, text_property, query, top_k=5):
    store = Neo4jVector.from_existing_index(
        embedding=text_embedding_model,
        url=NEO4J_URL,
        username=NEO4J_USER,
        password=NEO4J_PASSWORD,
        index_name=index_name,
        node_label=node_label,
        text_node_property=text_property
    )
    results = store.similarity_search_with_score(query, k=top_k)
    logger.info(f"Neo4j results for '{index_name}': {results}")
    return results