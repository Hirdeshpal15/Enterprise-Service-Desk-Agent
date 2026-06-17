# Tool Agent Flow

## Overview

The Tool Agent allows the assistant to perform actions instead of only answering questions.

Examples:

- Create support tickets
- Check ticket status
- Submit password reset requests

---

## Processing Flow

User Request
↓
GPT Intent Classification
↓
GPT Tool Selection
↓
Argument Extraction
↓
Tool Execution
↓
Result

---

## Intent Classification

The system determines whether the request is:

- Knowledge Request (RAG)
- Action Request (Tool)

Examples:

"What is the password policy?"
→ RAG

"Create a VPN support ticket."
→ Tool

---

## Tool Selection

GPT determines which tool should be executed.

Available Tools:

- create_ticket
- ticket_status
- password_reset

---

## Argument Extraction

GPT extracts required parameters from the user's request.

Example:

User:

Create a VPN ticket because I cannot connect.

Extracted Arguments:

- Tool: create_ticket
- Issue Type: VPN
- Description: Cannot connect

---

## Tool Execution

The selected tool executes the requested action.

Example:

create_ticket()

Result:

Ticket ID: INC-12345

Status: Open

---

## Benefits

- Natural language interaction
- Dynamic tool selection
- Action-oriented workflows
- Extensible architecture
