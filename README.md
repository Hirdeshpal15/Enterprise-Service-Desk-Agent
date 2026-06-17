# Enterprise Service Desk Agent

An AI-powered Enterprise Service Desk Assistant built using Azure AI Foundry, Azure OpenAI, Retrieval-Augmented Generation (RAG), and Tool Calling.

The project demonstrates the evolution of an enterprise AI assistant from a prompt-based chatbot to a unified agent capable of answering company policy questions and performing support actions.

---

## Features

### V1 - Prompt Agent

- IT support guidance
- Password assistance
- VPN troubleshooting guidance
- Software request guidance
- Access request guidance

### V2 - RAG Agent

- Company knowledge base integration
- Policy-aware responses
- Grounded answers
- Reduced hallucinations

Knowledge Sources:

- Password Policy
- VPN Policy
- Access Management Policy
- Software Request Policy

### V3 - Unified Agent

Combines:

- Retrieval-Augmented Generation (RAG)
- GPT-powered Tool Selection
- GPT-powered Argument Extraction
- GPT Intent Classification

Available Tools:

- Create Ticket
- Check Ticket Status
- Password Reset Request

---

## Architecture

```text
User
 ↓
GPT Intent Classifier
 ↓
 ┌───────────────┬───────────────┐
 │               │
RAG Path       Tool Path
 │               │
Knowledge      GPT Tool Selection
Retrieval      ↓
 ↓             Argument Extraction
GPT Response   ↓
               Tool Execution
```

---

## Project Structure

```text
Enterprise-Service-Desk-Agent
│
├── docs/
│   ├── architecture.md
│   ├── rag-flow.md
│   └── tool-agent-flow.md
│
├── knowledge_base/
│   ├── access_management_policy.md
│   ├── password_policy.md
│   ├── software_request_policy.md
│   └── vpn_policy.md
│
├── src/
│   ├── agents/
│   │   ├── it_service_desk_agent/
│   │   ├── service_desk_rag_agent/
│   │   ├── service_desk_tool_agent/
│   │   └── unified_service_desk_agent/
│   │
│   └── tools/
│       ├── create_ticket.py
│       ├── ticket_status.py
│       └── password_reset.py
│
└── infra/
```

---

## Technologies Used

- Azure AI Foundry
- Azure OpenAI GPT-4.1
- Azure AI Projects SDK
- Azure Monitor
- Application Insights
- Python
- GitHub
- Azure Developer CLI (azd)

---

## Running the Project

### Provision Azure Resources

```bash
azd up
azd env refresh
cp .azure/servicedesk-dev/.env .env
```

Add:

```env
AGENT_NAME=service-desk-v1
MODEL_NAME=gpt-4.1
```

---

### Run the Unified Agent

```bash
python -m src.agents.unified_service_desk_agent.unified_agent
```

---

## Example Questions

### RAG Questions

```text
What is the password policy?
```

```text
How do I request VPN access?
```

### Tool Requests

```text
Create a VPN support ticket.
```

```text
Reset password for john.smith.
```

```text
Check status for ticket INC-55555.
```

---

## Documentation

Additional documentation is available in:

- docs/architecture.md
- docs/rag-flow.md
- docs/tool-agent-flow.md

---

## Future Enhancements

- Azure AI Search integration
- ServiceNow integration
- Multi-agent architecture
- Human-in-the-loop workflows
- Enterprise ticketing system integration

---

## Learning Objectives

This project was built to learn:

- Prompt Engineering
- Azure AI Foundry
- Agent Development
- Retrieval-Augmented Generation (RAG)
- Tool Calling
- Evaluation and Monitoring
- GenAIOps Fundamentals
