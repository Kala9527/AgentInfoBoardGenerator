# NewsForge Agent

> A compact LangChain experiment for turning a user brief into news-search keywords and downstream article workflow data.

NewsForge Agent is the cleaned-up public name for this repository. It focuses on a small but useful AI workflow: load environment configuration, call a Zhipu-compatible OpenAI endpoint through LangChain, and parse structured model output for search and writing agents.

## Features

- Environment-based API configuration
- LangChain prompt chain for search keyword generation
- JSON code-block parser utility
- Starter structure for search, outline, and article generation agents

## Quick Start

Use Python 3.10+.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and set your real API keys.

```bash
python -m agents.search_agent
```

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Configuration

```text
ZHIPU_API_KEY   Zhipu API key
SERPER_API_KEY  Optional search provider key
SEARCH_K        Search result count, default 5
ENV             Environment suffix for .env.{ENV}
```

Secrets are intentionally excluded from Git. If an API key was committed before this cleanup, rotate it in the provider dashboard.

## Project Structure

```text
newsforge-agent/
|-- agents/
|   `-- search_agent.py
|-- config/
|   `-- config.py
|-- load_env.py
|-- llm.py
|-- utils.py
|-- requirements.txt
`-- .env.example
```

## Naming

The repository can stay as `jbsc`, but the public project name is now **NewsForge Agent**. Rename candidates:

- `newsforge-agent`
- `langchain-news-workflow`
- `ai-news-search-agent`

## Dependency Policy

No virtual environments, IDE settings, local `.env` files, generated output, or cache directories should be committed. Recreate dependencies with:

```bash
pip install -r requirements.txt
```
