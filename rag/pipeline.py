from rag.embeddings import create_embedding
from rag.retriever import retrieve_chunks


def build_prompt(question, chunks):
    context_parts = []

    for chunk in chunks:
        context_parts.append(
            f"[Source: {chunk['source']}, Page: {chunk['page']}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    return prompt


def generate_answer(prompt):
    # Temporary fake LLM response for local testing.
    # Replace this with the real LLM call when API credits are available.
    return "This is a test answer generated from the retrieved context."


def answer_question(question):
    query_vector = create_embedding(question)

    chunks = retrieve_chunks(query_vector, top_k=3)

    prompt = build_prompt(question, chunks)

    answer = generate_answer(prompt)

    return answer