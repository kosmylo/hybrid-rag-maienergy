from langchain_community.embeddings import SentenceTransformerEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL")

text_embedding_model = SentenceTransformerEmbeddings(
    model_name=EMBEDDING_MODEL_NAME
)

def embed_text(query):
    return text_embedding_model.embed_query(query)