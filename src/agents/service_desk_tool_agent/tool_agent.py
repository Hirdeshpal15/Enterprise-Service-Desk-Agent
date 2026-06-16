from src.agents.service_desk_tool_agent.tool_router import determine_action

from src.tools.create_ticket import create_ticket
from src.tools.ticket_status import get_ticket_status
from src.tools.password_reset import request_password_reset


def handle_request(user_input: str):

    action = determine_action(user_input)

    if action == "create_ticket":
        return create_ticket(
            issue_type="General Issue",
            description=user_input,
        )

    elif action == "ticket_status":
        return get_ticket_status("INC-10001")

    elif action == "password_reset":
        return request_password_reset("test.user")

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