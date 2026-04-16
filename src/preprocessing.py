from typing import List, Dict
from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text(text: str) -> str:
    """
    Basic text cleaning.
    """
    if not text:
        return ""

    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text.strip()


def clean_documents(documents: List[Dict]) -> List[Dict]:
    """
    Clean text in all loaded documents.
    """
    cleaned_docs = []

    for doc in documents:
        cleaned_docs.append(
            {
                "text": clean_text(doc["text"]),
                "metadata": doc["metadata"],
            }
        )

    return cleaned_docs


def chunk_documents(
    documents: List[Dict],
    chunk_size: int = 500,
    chunk_overlap: int = 100,
) -> List[Dict]:
    """
    Split document text into smaller chunks while preserving metadata.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunked_docs = []

    for doc in documents:
        text = doc["text"]
        metadata = doc["metadata"]

        if not text.strip():
            continue

        chunks = splitter.split_text(text)

        for i, chunk in enumerate(chunks):
            chunked_docs.append(
                {
                    "text": chunk,
                    "metadata": {
                        **metadata,
                        "chunk_id": i,
                    },
                }
            )

    return chunked_docs