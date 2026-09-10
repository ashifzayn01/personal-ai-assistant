# Personal AI Assistant

A multi-stage AI engineering project built step-by-step, starting from a basic AI chat system and evolving toward a personal AI assistant.

## Project Evolution

### V1 — AI Chat CLI
- Basic AI conversation
- OpenAI integration
- Conversation memory
- Prompt handling
- Error handling

### V2 — Memory + Tools
- SQLite database
- CRUD operations for notes
- Tool functions
- Tool registry
- Dynamic tool argument validation

### V3 — FastAPI AI Backend
- FastAPI application
- API routes
- Pydantic request/response models
- HTTP status handling
- APIRouter-based structure
- Swagger/OpenAPI testing

### V4 — RAG Document Assistant
- PDF text extraction
- Page-aware chunking
- Chunk metadata
- Embedding interface
- Chroma vector store
- Vector retrieval
- Context construction
- Prompt construction
- End-to-end RAG pipeline

## Project 4 Architecture

PDF
→ PDF Loader
→ Chunks + Metadata
→ Embeddings
→ Chroma Vector Store
→ Retriever
→ Context
→ LLM
→ Answer

## Current Project 4 Status

The RAG architecture and local pipeline have been implemented and tested.

Real embedding generation and live LLM generation are currently represented by temporary placeholders because live API access is unavailable due to API quota.

## Planned Evolution

V5 — Tool-Using AI Agent

Then:
- LangChain
- LangGraph
- Advanced agent orchestration

Final goal:
- Personal AI Assistant