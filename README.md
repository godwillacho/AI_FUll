# Applied AI Engineering

Hands-on work with large language models: retrieval-augmented generation, tool-using agents, structured outputs, prompt engineering, and serving local models, built on a foundation of concurrent and asynchronous Python.

## Featured Project: Security+ RAG Study Assistant (`rag/`)

A retrieval-augmented generation (RAG) assistant that answers CompTIA Security+ questions from an indexed study guide, cites the page numbers to read, and generates practice questions.

```
PDF ──► PyPDFLoader ──► Text splitter ──► OpenAI embeddings ──► Qdrant (Docker)
                                                                    │
User question ──► Embed ──► Similarity search (top 4 chunks) ◄──────┘
                                    │
                                    ▼
                         LLM answers from context only,
                         with page references
```

**Stack:** Python, LangChain, OpenAI (`text-embedding-3-large`), Qdrant, Docker Compose

**Design choices**
- 1,000-character chunks with 400-character overlap, so definitions that span a chunk boundary are still retrieved intact.
- The model is instructed to answer only from retrieved context and to say when the answer is not there, which keeps it grounded in the study material.
- Qdrant runs in a container with a persistent volume, so the index survives restarts.

**Run it**
```bash
cd rag
cp ../.env.example ../.env            # add your OPENAI_API_KEY
docker compose up -d                   # start Qdrant on localhost:6333
pip install -r requirements.txt
python index.py path/to/study_guide.pdf   # build the index (bring your own PDF)
python chat.py
```

## Other Work

| Folder | What it covers |
|---|---|
| `Agentic_AI/` | Tool-calling agents with a plan, act, observe loop; Pydantic-validated structured outputs; chain-of-thought prompting with a live weather tool |
| `Ai_core/openai/` | Tokenisation, zero-shot, persona and chain-of-thought prompting; using Gemini through the OpenAI-compatible API |
| `Ai_core/openai/ollama_fastapi/` | Serving a local Gemma model through Ollama behind a FastAPI endpoint |
| `fundamentals/` | Threading, multiprocessing, locks and queues, asyncio, generators, decorators, comprehensions, and CSV processing |

## Setup

All API keys are read from environment variables. Copy `.env.example` to `.env` and add your own keys; `.env` is ignored by git.

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r Agentic_AI/requirements.txt
```
