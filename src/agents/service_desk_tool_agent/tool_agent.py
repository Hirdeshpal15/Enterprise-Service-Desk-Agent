from src.agents.service_desk_tool_agent.gpt_router import determine_action

from src.tools.create_ticket import create_ticket
from src.tools.ticket_status import get_ticket_status
from src.tools.password_reset import request_password_reset


def handle_request(user_input: str):

    routing_result = determine_action(user_input)

    action = routing_result["tool"]

    if action == "create_ticket":

        issue_type = routing_result.get(
            "issue_type",
            "General Issue"
        )

        description = routing_result.get(
            "description",
            user_input
        )

        return create_ticket(
            issue_type=issue_type,
            description=description,
        )


    elif action == "ticket_status":

        ticket_id = routing_result.get(
            "ticket_id",
            "INC-10001"
        )

        return get_ticket_status(ticket_id)

    elif action == "password_reset":

        username = routing_result.get(
            "username",
            "test.user"
        )

        return request_password_reset(username)

    return {
        "message": "I could not determine the correct action."
    }


if __name__ == "__main__":

    while True:

        user_input = input("\nRequest: ")

        if user_input.lower() in ["quit", "exit"]:
            break

        result = handle_request(user_input)

        print("\nResult:")
        print(result)