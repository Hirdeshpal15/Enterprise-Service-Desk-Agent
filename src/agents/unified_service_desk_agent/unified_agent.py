from src.agents.unified_service_desk_agent.gpt_intent_router import (
    determine_intent
)

# V2 RAG Agent
from src.agents.service_desk_rag_agent.rag_agent import ask

# V3 Tool Agent
from src.agents.service_desk_tool_agent.tool_agent import (
    handle_request
)


def process_request(user_input: str):

    intent_result = determine_intent(user_input)

    intent = intent_result["intent"]

    if intent == "tool":
        return {
            "type": "tool",
            "result": handle_request(user_input)
        }

    return {
        "type": "rag",
        "result": ask(user_input)
    }


if __name__ == "__main__":

    while True:

        user_input = input("\nRequest: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        result = process_request(user_input)

        print("\nResponse:")
        if result["type"] == "rag":

            rag_result = result["result"]

            print("\nPath: RAG")
            print(f"Document: {rag_result['document']}")
            print("\nAnswer:")
            print(rag_result["answer"])

        else:

            print("\nPath: TOOL")
            print("\nResult:")
            print(result["result"])