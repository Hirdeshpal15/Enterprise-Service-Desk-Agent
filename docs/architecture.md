# Enterprise Service Desk Agent Architecture

## Project Overview

The Enterprise Service Desk Agent demonstrates the evolution of an AI-powered IT support assistant using Azure AI Foundry, Azure OpenAI, Retrieval-Augmented Generation (RAG), and Tool Calling.

The project progresses through multiple stages:

- V1: Prompt-Based Agent
- V2: RAG Agent
- V3: Unified Agent (RAG + Tools)

---

## V1 - Prompt Agent

Architecture:

User
↓
GPT-4.1
↓
Response

Capabilities:

- IT support guidance
- VPN troubleshooting assistance
- Password assistance
- Software request guidance
- Access request guidance

Limitations:

- No company-specific knowledge
- No action execution
- Answers depend only on the prompt

---

## V2 - RAG Agent

Architecture:

User
↓
Retriever
↓
Knowledge Base
↓
GPT-4.1
↓
Grounded Response

Knowledge Base Documents:

- VPN Policy
- Password Policy
- Access Management Policy
- Software Request Policy

Capabilities:

- Uses company policies as context
- Produces grounded responses
- Reduces hallucinations
- Retrieves relevant information before generating answers

---

## V3 - Unified Service Desk Agent

Architecture:

User
↓
GPT Intent Classifier
↓
├── RAG Path
│ ↓
│ Knowledge Retrieval
│ ↓
│ GPT Response
│
└── Tool Path
↓
GPT Tool Selection
↓
Argument Extraction
↓
Tool Execution
↓
Result

Available Tools:

- Create Ticket
- Check Ticket Status
- Password Reset Request

Capabilities:

- Answers policy questions
- Creates support tickets
- Checks ticket status
- Submits password reset requests

---

## Technologies Used

- Azure AI Foundry
- Azure OpenAI GPT-4.1
- Python
- Azure AI Projects SDK
- Application Insights
- Azure Monitor
- GitHub
- Azure Developer CLI (azd)

---

## Future Enhancements

- Azure AI Search integration
- Enterprise ticketing system integration
- Multi-agent architecture
- Human-in-the-loop workflows
- Advanced evaluation pipelines
