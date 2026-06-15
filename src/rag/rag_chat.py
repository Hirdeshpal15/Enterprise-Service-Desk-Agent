import os
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

load_dotenv()

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
    api_version="2024-10-21",
)

KNOWLEDGE_DIR = Path("knowledge_base")


def load_documents():
    docs = {}

    for file in KNOWLEDGE_DIR.glob("*.md"):
        docs[file.name] = file.read_text()

    return docs


def retrieve(query, documents):
    query_words = query.lower().split()

    matches = []

    for filename, content in documents.items():
        score = sum(
            1 for word in query_words
            if word in content.lower()
        )

        matches.append((score, filename, content))

    matches.sort(reverse=True)

    return matches[0]


documents = load_documents()

while True:
    question = input("\nQuestion: ")

    if question.lower() in ["exit", "quit"]:
        break

    score, filename, context = retrieve(question, documents)

    print(f"\nRetrieved: {filename}")

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "gpt-4.1"),
        messages=[
            {
                "role": "system",
                "content": """
You are an Enterprise Service Desk Assistant.

Answer ONLY using the provided company policy.

If the answer is not found in the policy,
say that the information is unavailable.
"""
            },
            {
                "role": "user",
                "content": f"""
Company Policy:

{context}

Question:

{question}
"""
            }
        ]
    )

    print("\nAnswer:")
    print(response.choices[0].message.content)