from typing import List, Dict
from src.embedding import build_vector_store


def retrieve_relevant_chunks(
    query: str,
    chunks: List[Dict],
    top_k: int = 3
) -> List[Dict]:
    """
    Retrieve the most relevant chunks for a user query.
    """
    vector_store, _ = build_vector_store(chunks)

    results = vector_store.similarity_search(query, k=top_k)

    retrieved_chunks = []

    for doc in results:
        retrieved_chunks.append(
            {
                "text": doc.page_content,
                "metadata": doc.metadata
            }
        )

    return retrieved_chunks