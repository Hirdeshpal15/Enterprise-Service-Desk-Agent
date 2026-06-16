import json
import os

from dotenv import load_dotenv
from azure.identity import (
    DefaultAzureCredential,
    get_bearer_token_provider,
)
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

SYSTEM_PROMPT = """
You are an intent classification assistant.

Classify the user's request into exactly one category.

Categories:

rag
- User is asking for information
- User wants to understand a process
- User is asking about company policy
- User wants guidance or instructions

tool
- User wants an action performed
- User wants a ticket created
- User wants a password reset
- User wants ticket status checked
- User wants a request submitted

Return ONLY valid JSON.

Examples:

{"intent":"rag"}

{"intent":"tool"}
"""


def determine_intent(user_input: str):
    """
    Determine whether a request should go
    through the RAG path or Tool path.
    """

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "gpt-4.1"),
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    print("\nGPT Intent Decision:")
    print(content)

    try:
        result = json.loads(content)

        if result.get("intent") not in ["rag", "tool"]:
            return {"intent": "rag"}

        return result

    except Exception:
        return {"intent": "rag"}


if __name__ == "__main__":

    test_queries = [
        "How do I request VPN access?",
        "What is the password policy?",
        "Create a VPN support ticket",
        "Reset password for john.smith",
        "Check status for ticket INC-55555",
    ]

    for query in test_queries:

        print("\n" + "=" * 60)
        print(f"Query: {query}")

        result = determine_intent(query)

        print(f"Intent: {result['intent']}")