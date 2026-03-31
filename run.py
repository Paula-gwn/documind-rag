from src.pipeline import run_ingestion_pipeline


def main():
    data_dir = "data"
    chunks = run_ingestion_pipeline(data_dir)

    print(f"Loaded and chunked {len(chunks)} chunks.\n")

    for i, chunk in enumerate(chunks[:5], start=1):
        print(f"--- Chunk {i} ---")
        print("Metadata:", chunk["metadata"])
        print("Text:", chunk["text"][:300])
        print()


if __name__ == "__main__":
    main()