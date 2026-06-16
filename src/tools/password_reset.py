def request_password_reset(username: str):
    return {
        "username": username,
        "request_status": "Submitted",
        "approval_required": False,
    }