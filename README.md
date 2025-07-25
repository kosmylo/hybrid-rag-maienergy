# 🔍 mAiEnergy Hybrid RAG Repository

This repository provides a robust **Hybrid Retrieval-Augmented Generation (RAG)** framework for the **mAiEnergy project**. It seamlessly integrates multimodal and structured data from:

- 📝 **OpenSearch** (Textual and numerical data)
- 🖼️ **Milvus** (Multimodal image embeddings)
- 🔗 **Neo4j** (Structured knowledge graph embeddings)

## 📂 Repository Structure

```plaintext
maienergy-hybrid-rag
├── .env # Environment variables
├── .gitignore
├── README.md
├── config
│ └── db_config.py # Dataset & DB configurations
├── embeddings
│ ├── multimodal_embeddings.py # CLIP multimodal embeddings
│ └── text_embeddings.py # Sentence-transformer embeddings
├── main.py # Main script for running the hybrid RAG
├── requirements.txt # Python dependencies
├── retrievers
│ ├── hybrid_retriever.py # Unified retrieval and ranking logic
│ ├── milvus_retriever.py # Milvus retriever for images
│ ├── neo4j_retriever.py # Neo4j retriever for knowledge graphs
│ └── opensearch_retriever.py # OpenSearch retriever for textual data
└── utils
└── fusion.py # Result fusion logic (Weighted RRF)
```

## 🚀 Getting Started

### **Step 1: Clone the Repository**

```bash
git clone <your-repo-url>
cd maienergy-hybrid-rag
```

### **Step 2: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 3: Configure Your Environment**

Create and edit your `.env` file:

```bash
OPENSEARCH_HOST=http://<VM_IP>:9200
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDING_DIMENSION=384

MILVUS_HOST=<VM_IP>
MILVUS_PORT=19530
EMBED_DIMENSION=768
CLIP_MODEL_NAME=openai/clip-vit-large-patch14-336

NEO4J_URL=bolt://<VM_IP>:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=<password>
```

Adjust these values according to your deployment.

## 🧩 Key Components Explained

### 🔖 Embeddings

- `text_embeddings.py`: Embedding textual data with SentenceTransformers.

- `multimodal_embeddings.py`: Embedding multimodal queries (text-to-image) with CLIP.

### 🔍 Retrievers

| Retriever                 | Description                         | Data Source                  |
| ------------------------- | ----------------------------------- | ---------------------------- |
| `opensearch_retriever.py` | Semantic + keyword hybrid retrieval | OpenSearch (text/numerical)  |
| `milvus_retriever.py`     | Multimodal vector search            | Milvus (images & embeddings) |
| `neo4j_retriever.py`      | Graph-based vector search           | Neo4j (knowledge graph)      |
| `hybrid_retriever.py`     | Unified retrieval from all sources  | OpenSearch, Milvus, Neo4j    |

### 🎛️ Fusion Logic

- `fusion.py`: Implements Weighted Reciprocal Rank Fusion (WRRF) to intelligently combine results from multiple retrieval sources into a single unified ranking.