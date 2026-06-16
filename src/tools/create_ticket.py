from datetime import datetime
import random


def create_ticket(issue_type: str, description: str):
    ticket_id = f"INC-{random.randint(10000,99999)}"

    return {
        "ticket_id": ticket_id,
        "issue_type": issue_type,
        "status": "Open",
        "created_at": datetime.now().isoformat(),
        "description": description,
    }