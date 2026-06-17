# RAG Flow

## What is RAG?

Retrieval-Augmented Generation (RAG) combines knowledge retrieval with large language models.

Instead of relying only on the model's training data, the agent retrieves relevant company information before generating a response.

---

## Knowledge Sources

The knowledge base contains:

- VPN Policy
- Password Policy
- Access Management Policy
- Software Request Policy

---

## RAG Processing Flow

User Question
↓
Retriever
↓
Knowledge Base Search
↓
Relevant Document / Chunk
↓
GPT-4.1
↓
Grounded Response

---

## Chunking

Documents are split into smaller chunks.

Benefits:

- Better retrieval accuracy
- Lower token usage
- Faster context selection
- Improved scalability

---

## Retrieval

The retriever searches available chunks and selects the most relevant content for the user's question.

Example:

Question:

How do I request Adobe Acrobat?

Retrieved Document:

software_request_policy.md

---

## Grounding

Retrieved content is injected into the prompt.

This ensures that responses are based on company policies instead of model assumptions.

---

## Benefits

- Reduces hallucinations
- Uses company-specific knowledge
- Improves response accuracy
- Provides policy-aligned answers
