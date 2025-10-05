# Copilot Instructions for AI Coding Agents

## Project Overview
This workspace contains two major Python learning projects:
- **python-udemy-main**: A comprehensive Python course with modular chapters, challenges, and practical scripts. Organized by topic (datatypes, conditionals, loops, functions, OOP, exceptions, etc.), each in its own folder. Includes hands-on CLI tools, automation scripts, and data handling exercises.
- **udemy-genai-python-main**: Focused on generative AI, LLMs, and agent-based workflows. Contains subprojects for RAG (Retrieval-Augmented Generation), voice agents, LangChain, and more. Uses modern AI/ML libraries and OpenAI APIs.

## Key Architectural Patterns
- **Modular Structure**: Each topic or project is in its own folder. Scripts are self-contained, often with their own data files (CSV, JSON, etc.).
- **Challenge-Driven Learning**: Many folders (e.g., `challenges/`) contain real-world mini-apps (contact books, file organizers, credential managers) with clear requirements in docstrings.
- **AI/LLM Integrations**: The `udemy-genai-python-main` project uses LangChain, OpenAI, Qdrant, and dotenv for environment/config management. RAG and agent workflows are in `rag/`, `rag_queue/`, and `voice_agent/`.
- **Data Handling**: Frequent use of CSV, JSON, and file I/O. Many scripts auto-create data files if missing.
- **Environment Variables**: Sensitive keys (API, etc.) are loaded via `.env` using `dotenv`.

## Developer Workflows
- **Run Scripts**: Most scripts are CLI-based. Run directly with `python script.py` from the appropriate folder.
- **Install Dependencies**:
  - For classic Python: `pip install -r requirements.txt` (see `01_virtual/requirements.txt` and `udemy-genai-python-main/requirements.txt`).
  - For AI/LLM projects: Ensure Qdrant is running (for RAG), and set up `.env` with required API keys.
- **Testing**: No formal test suite; validate by running scripts and following CLI prompts.
- **Debugging**: Use print statements or Python debuggers. Many scripts have clear error messages and input validation.

## Project-Specific Conventions
- **File Naming**: Scripts are named by topic and order (e.g., `chapter_1.py`, `day_4.py`).
- **Data Files**: CSV/JSON files are created in the script's directory. Avoid hardcoding paths; use relative paths or `os.path` utilities.
- **API Keys**: Never commit real API keys. Use `.env` and `dotenv` for secrets.
- **No Central Entry Point**: Each script is standalone unless otherwise noted.

## Integration Points
- **LangChain/OpenAI**: Used in `rag/`, `rag_queue/`, and `voice_agent/` for LLM and embedding workflows.
- **Qdrant**: Vector DB for RAG; must be running locally for those scripts.
- **Speech Recognition**: `voice_agent/` uses `speech_recognition` and OpenAI TTS.

## Examples
- See `challenges/02_data_handling/day_4.py` for API+CSV logging.
- See `rag/index.py` for a minimal RAG pipeline with LangChain and Qdrant.
- See `voice_agent/main.py` for a voice-to-LLM-to-speech agent.

## Tips for AI Agents
- Prefer adding new scripts in the relevant topic folder.
- Follow the docstring requirements in challenge scripts.
- When adding AI features, use `.env` for secrets and document new dependencies.
- Reference existing scripts for CLI/UX patterns and data handling.
