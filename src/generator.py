import re
from typing import List, Dict
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def format_context(retrieved_chunks: List[Dict]) -> str:
    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        source = chunk["metadata"].get("source", "unknown")
        page = chunk["metadata"].get("page", "unknown")
        text = chunk["text"]

        context_parts.append(
            f"[Source {i} | file={source} | page={page}]\n{text}"
        )

    return "\n\n".join(context_parts)


def extract_fields_from_context(context: str) -> str:
    owner_match = re.search(r"project owner is ([A-Za-z]+(?: [A-Za-z]+)*)", context, re.IGNORECASE)
    budget_match = re.search(r"\$[\d,]+", context)

    owner = owner_match.group(1) if owner_match else "Not found"
    budget = budget_match.group(0) if budget_match else "Not found"

    return f"Project owner: {owner}\nBudget: {budget}"


def generate_answer(query: str, retrieved_chunks: List[Dict]) -> str:
    context = format_context(retrieved_chunks)

    prompt = f"""
You are answering a question using only the provided context.

Instructions:
- Extract all relevant facts needed to answer the full question.
- If the question asks for multiple items, answer all of them.
- Do not omit values if they are present in the context.
- If a fact is missing, say "Not found".
- Return the answer exactly in this format:

Project owner: <value>
Budget: <value>

Question:
{query}

Context:
{context}

Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=False
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    has_owner = "project owner:" in answer.lower()
    has_budget = "budget:" in answer.lower() and "$" in answer

    if has_owner and has_budget:
        return answer

    return extract_fields_from_context(context)