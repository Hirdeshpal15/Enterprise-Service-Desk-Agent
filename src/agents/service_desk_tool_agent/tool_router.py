def determine_action(user_input: str):
    text = user_input.lower()

    if "ticket status" in text:
        return "ticket_status"

    if "password" in text and "reset" in text:
        return "password_reset"

    if "create" in text and "ticket" in text:
        return "create_ticket"

    return "unknown"