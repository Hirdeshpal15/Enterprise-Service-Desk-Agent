"""
V3.1 GPT-Powered Tool Router
"""



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
You are a tool routing assistant.

Available tools:

1. create_ticket
2. ticket_status
3. password_reset

Return ONLY valid JSON.

Examples:

{
  "tool": "create_ticket",
  "issue_type": "VPN",
  "description": "Cannot connect to VPN"
}

{
  "tool": "ticket_status",
  "ticket_id": "INC-10001"
}

{
  "tool": "password_reset",
  "username": "john.smith"
}
"""


def determine_action(user_input: str):

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
    print("\nGPT Routing Decision:")
    print(content)

    try:
        return json.loads(content)
    except Exception:
        return {
            "tool": "unknown"
        }