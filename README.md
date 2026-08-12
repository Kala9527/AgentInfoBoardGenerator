# NewsForge Agent 新闻生成智能体

> 一个基于 LangChain 的新闻选题搜索关键词生成与文章工作流实验项目。

[English README](./README.en.md)

NewsForge Agent 是 `jbsc` 仓库整理后的公开项目名。项目聚焦一个轻量但实用的 AI 工作流：读取环境配置，通过 OpenAI 兼容接口调用智谱模型，并解析模型输出的结构化 JSON，为后续搜索、提纲和文章生成智能体提供基础。

## 项目亮点

- 使用环境变量管理 API Key，避免密钥进入仓库
- 基于 LangChain 的搜索关键词生成链
- 提供 JSON 代码块解析工具
- 预留搜索、提纲、正文生成等智能体工作流结构
- 已清理 `.env`、`.idea`、本地缓存和无效杂项文件

## 快速开始

请使用 Python 3.10 或更高版本。

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

编辑 `.env`，填入自己的 API Key，然后运行：

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

## 配置项

```text
ZHIPU_API_KEY   智谱开放平台 API Key
SERPER_API_KEY  可选，搜索服务 API Key
SEARCH_K        搜索结果数量，默认 5
ENV             环境后缀，例如 development
```

密钥文件不会提交到 Git。若历史中曾经提交过真实 API Key，请在服务商后台重置该 Key。

## 项目结构

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

## 命名建议

仓库名可以继续保留为 `jbsc`，但项目展示名已经整理为 **NewsForge Agent / 新闻生成智能体**。如果后续想重命名 GitHub 仓库，可以考虑：

- `newsforge-agent`
- `langchain-news-workflow`
- `ai-news-search-agent`

## 依赖管理说明

以下内容不会提交到仓库：

- `.env`、`.env.*`
- `.venv/`、`venv/`
- `.idea/`
- `__pycache__/`
- `output/`、`logs/`

如需恢复依赖，执行：

```bash
pip install -r requirements.txt
```
