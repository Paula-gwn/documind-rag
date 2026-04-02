# First run.py for Phase1
# from src.pipeline import run_ingestion_pipeline


# def main():
#     data_dir = "data"
#     chunks = run_ingestion_pipeline(data_dir)

#     print(f"Loaded and chunked {len(chunks)} chunks.\n")

#     for i, chunk in enumerate(chunks[:5], start=1):
#         print(f"--- Chunk {i} ---")
#         print("Metadata:", chunk["metadata"])
#         print("Text:", chunk["text"][:300])
#         print()


# if __name__ == "__main__":
#     main()

# Phase 2 run.py
from src.pipeline import run_ingestion_pipeline
from src.retriever import retrieve_relevant_chunks


def main():
    data_dir = "data"
    chunks = run_ingestion_pipeline(data_dir)

    print(f"\nLoaded and chunked {len(chunks)} chunks.\n")

    query = "Who is the project owner and what is the budget?"
    results = retrieve_relevant_chunks(query=query, chunks=chunks, top_k=2)

    print(f"Query: {query}\n")
    print("Top retrieved chunks:\n")

    for i, chunk in enumerate(results, start=1):
        print(f"--- Result {i} ---")
        print("Metadata:", chunk["metadata"])
        print("Text:", chunk["text"])
        print()


if __name__ == "__main__":
    main()