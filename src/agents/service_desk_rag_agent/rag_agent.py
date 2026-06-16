import os
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import (
    DefaultAzureCredential,
    get_bearer_token_provider
)
from openai import AzureOpenAI

from src.agents.service_desk_rag_agent.retriever import PolicyRetriever

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

knowledge_dir = (
    Path(__file__).parent
    / "knowledge"
)

retriever = PolicyRetriever(knowledge_dir)


SYSTEM_PROMPT = """
You are an Enterprise Service Desk Assistant.

Use the supplied company policy
to answer the user's question.

Rules:

- Follow company procedures.
- Follow security best practices.
- Do not invent policies.
- If the policy does not contain the answer,
  clearly state that.
"""


def ask(question: str):
    retrieval_result = retriever.retrieve(question)

    context = retrieval_result["content"]

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "gpt-4.1"),
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
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

    return {
        "document": retrieval_result["document"],
        "chunk_id": retrieval_result["chunk_id"],
        "answer": response.choices[0].message.content,
    }


if __name__ == "__main__":
    while True:
        question = input("\nQuestion: ")

        if question.lower() in ["exit", "quit"]:
            break

        result = ask(question)

        print(
            f"\nRetrieved: "
            f"{result['document']} "
            f"(chunk {result['chunk_id']})"
        )
        print("\nAnswer:")
        print(result["answer"])