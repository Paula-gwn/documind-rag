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
# from src.pipeline import run_ingestion_pipeline
# from src.retriever import retrieve_relevant_chunks


# def main():
#     data_dir = "data"
#     chunks = run_ingestion_pipeline(data_dir)

#     print(f"\nLoaded and chunked {len(chunks)} chunks.\n")

#     query = "Who is the project owner and what is the budget?"
#     results = retrieve_relevant_chunks(query=query, chunks=chunks, top_k=2)

#     print(f"Query: {query}\n")
#     print("Top retrieved chunks:\n")

#     for i, chunk in enumerate(results, start=1):
#         print(f"--- Result {i} ---")
#         print("Metadata:", chunk["metadata"])
#         print("Text:", chunk["text"])
#         print()


# if __name__ == "__main__":
#     main()

#Phase 3 the G in RAG
from src.pipeline import run_ingestion_pipeline
from src.retriever import retrieve_relevant_chunks
from src.generator import generate_answer


def main():
    data_dir = "data"
    query = "What is the project owner and what is the estimated budget for phase one?"

    chunks = run_ingestion_pipeline(data_dir)
    retrieved_chunks = retrieve_relevant_chunks(query=query, chunks=chunks, top_k=2)
    answer = generate_answer(query=query, retrieved_chunks=retrieved_chunks)

    print(f"\nLoaded and chunked {len(chunks)} chunks.\n")
    print(f"Query: {query}\n")
    print("Retrieved chunks:\n")

    for i, chunk in enumerate(retrieved_chunks, start=1):
        print(f"--- Result {i} ---")
        print("Metadata:", chunk["metadata"])
        print("Text:", chunk["text"])
        print()

    print("Generated answer:\n")
    print(answer)


if __name__ == "__main__":
    main()