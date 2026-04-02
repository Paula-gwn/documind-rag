from typing import List, Dict
from src.ingestion import load_documents
from src.preprocessing import clean_documents, chunk_documents


def run_ingestion_pipeline(data_dir: str) -> List[Dict]:
    """
    End-to-end ingestion and preprocessing pipeline.
    """
    raw_documents = load_documents(data_dir)
    cleaned_documents = clean_documents(raw_documents)
    chunked_documents = chunk_documents(cleaned_documents)

    return chunked_documents