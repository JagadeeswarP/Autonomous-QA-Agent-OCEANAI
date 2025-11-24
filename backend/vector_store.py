import chromadb
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.PersistentClient(path="./chroma_db")

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_or_load_collection():
    try:
        return chroma_client.get_collection("qa_kb")
    except:
        return chroma_client.create_collection(
            name="qa_kb",
            metadata={"hnsw:space": "cosine"}  
        )

def add_to_vector_db(text, metadata):
    collection = create_or_load_collection()

    embedding = model.encode([text])[0].tolist()

    collection.add(
        ids=[metadata["id"]],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )

def similarity_search(query, top_k=5):
    collection = create_or_load_collection()

    q_emb = model.encode([query])[0].tolist()

    results = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k
    )

    return results
