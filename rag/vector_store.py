import chromadb


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks, vectors):
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    documents = [chunk["text"] for chunk in chunks]

    metadatas = [
        {
            "source": chunk["source"],
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=vectors,
        metadatas=metadatas
    )

    return len(chunks)


def search_chunks(query_vector, top_k=3):
    return collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )