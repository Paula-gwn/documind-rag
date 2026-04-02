from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader


def load_txt(file_path: Path) -> List[Dict]:
    """
    Load a TXT file and return it as a single document item.
    """
    text = file_path.read_text(encoding="utf-8")
    return [
        {
            "text": text,
            "metadata": {
                "source": file_path.name,
                "file_type": "txt",
                "page": 1,
            },
        }
    ]


def load_pdf(file_path: Path) -> List[Dict]:
    """
    Load a PDF file page by page and return a list of document items.
    Each item contains page text and metadata.
    """
    documents = []
    reader = PdfReader(str(file_path))

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        documents.append(
            {
                "text": text,
                "metadata": {
                    "source": file_path.name,
                    "file_type": "pdf",
                    "page": page_number,
                },
            }
        )

    return documents


def load_documents(data_dir: str) -> List[Dict]:
    """
    Load all supported documents from a directory.
    Supports .pdf and .txt files.
    """
    data_path = Path(data_dir)

    if not data_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    all_documents = []

    for file_path in data_path.iterdir():
        if file_path.suffix.lower() == ".pdf":
            all_documents.extend(load_pdf(file_path))
        elif file_path.suffix.lower() == ".txt":
            all_documents.extend(load_txt(file_path))

    return all_documents