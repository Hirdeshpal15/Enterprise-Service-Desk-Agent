def determine_intent(user_input: str):

    text = user_input.lower()

    action_keywords = [
        "create",
        "open",
        "reset",
        "status",
        "submit",
        "ticket",
    ]

    if any(keyword in text for keyword in action_keywords):
        return "tool"

    return "rag"