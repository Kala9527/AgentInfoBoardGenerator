# Agent Info Board Generator

> A multi-agent project for information organization and bulletin-board generation.

Agent Info Board Generator is a lightweight AI workflow project built around information collection, content organization, and board-style presentation. The current code provides a LangChain-based search keyword generation flow: it loads environment configuration, calls an OpenAI-compatible model endpoint, and parses structured JSON returned by the model.

The name is more formal than the original `jbsc` and describes the project goal directly: coordinate multiple agents to turn a user request into organized, readable, and display-ready information boards.

## Features

- Environment-based API key management.
- LangChain prompt chain for search keyword generation.
- Utility for parsing fenced JSON code blocks from model responses.
- Starter structure for search, outline, article/content, and board rendering agents.
- A practical foundation for a full flow: topic input -> information gathering -> content organization -> web board generation.

## Quick Start

Use Python 3.10+.

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and set your real API keys, then run:

```bash
python -m agents.search_agent
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m agents.search_agent
```

## Configuration

```text
ZHIPU_API_KEY   Zhipu API key
SERPER_API_KEY  Optional search provider key
SEARCH_K        Search result count, default 5
ENV             Environment suffix, for example development
```

Secrets are intentionally excluded from Git. If a real API key was ever committed, rotate it in the provider dashboard.

## Project Structure

```text
agent-info-board-generator/
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

## Roadmap Ideas

- Add a real search agent with Serper, Bing, Tavily, or a custom search provider.
- Add an outline agent that turns search results into a board structure.
- Add a writer agent for presentation-ready sections.
- Add a frontend page that renders generated content into a shareable web board.
- Add export support for HTML, Markdown, images, or PDF.

## Dependency Policy

No virtual environments, IDE settings, local `.env` files, generated output, or cache directories should be committed. Recreate dependencies with:

```bash
pip install -r requirements.txt
```

## Thanks

Thank you for checking out this project. Information organization and presentation are quiet but important parts of learning, reporting, and creating. If this project gives you a useful starting point, a Star, Fork, issue, or suggestion would be greatly appreciated.
