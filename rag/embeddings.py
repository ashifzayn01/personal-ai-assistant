def create_embedding(text):
    # Temporary vector for learning/testing.
    # Later this will be replaced with a real embedding model.
    return [0.12, -0.43, 0.87, 0.21]


def create_embeddings(chunks):
    vectors = []

    for chunk in chunks:
        vector = create_embedding(chunk["text"])
        vectors.append(vector)

    return vectors