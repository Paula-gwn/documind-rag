from typing import List, Dict, Tuple
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

def convert_to_langchain_documents(chunks: List[Dict]) -> List[Document]:
    """
    Convert chunk dictionaries into LangChain Document objects.
    """
    documents = []

    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk["text"],
                metadata=chunk["metadata"]
            )
        )
    return documents


def build_vector_store(chunks: List[Dict]) -> Tuple[FAISS, List[Document]]:
    """
    Convert chunks to embeddings and store them in a FAISS vector index.
    """
    documents = convert_to_langchain_documents(chunks)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(documents, embedding_model)

    return vector_store, documents