import os
from pathlib import Path

KNOWLEDGE_DIR = Path("knowledge_base")


def load_documents():
    documents = {}

    for file in KNOWLEDGE_DIR.glob("*.md"):
        with open(file, "r") as f:
            documents[file.name] = f.read()

    return documents


def retrieve(query, documents):
    query_words = query.lower().split()

    matches = []

    for filename, content in documents.items():
        score = 0

        for word in query_words:
            if word in content.lower():
                score += 1

        matches.append((score, filename, content))

    matches.sort(reverse=True)

    return matches[0]


if __name__ == "__main__":
    docs = load_documents()

    user_question = input("Question: ")

    score, filename, content = retrieve(user_question, docs)

    print("\nMost Relevant Document:")
    print(f"File: {filename}")
    print(f"Score: {score}")

    print("\nDocument Content:")
    print(content)