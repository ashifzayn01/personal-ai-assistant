from rag.vector_store import search_chunks


def retrieve_chunks(query_vector, top_k=3):
    result = search_chunks(query_vector, top_k)

    documents = result["documents"][0]
    metadatas = result["metadatas"][0]
    distances = result["distances"][0]

    chunks = []

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):
        chunks.append({
            "text": document,
            "source": metadata["source"],
            "page": metadata["page"],
            "distance": distance
        })

    return chunks