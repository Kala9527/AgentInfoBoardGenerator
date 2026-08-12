# Agent Info Board Generator

> 多 Agent 信息整理与板报生成展示项目。

[English README](./README.en.md)

Agent Info Board Generator 是一个围绕“信息收集、内容整理、板报生成”设计的轻量 AI 工作流项目。当前代码提供了基于 LangChain 的搜索关键词生成能力：读取环境配置，通过 OpenAI 兼容接口调用模型，并解析模型输出的结构化 JSON，为后续搜索、提纲、正文生成和 Web 板报展示打基础。

这个名称比原来的 `jbsc` 更正式，也更直接表达项目目标：让多个智能体协作，把用户需求整理成可展示、可阅读、可继续加工的信息板报。

## 功能亮点

- 使用环境变量管理 API Key，避免密钥进入仓库。
- 基于 LangChain 构建搜索关键词生成链。
- 支持解析模型返回的 fenced JSON 代码块。
- 预留搜索、提纲、正文生成、板报渲染等多 Agent 工作流结构。
- 适合继续扩展为“输入主题 -> 收集资料 -> 整理内容 -> 生成板报页面”的完整应用。

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

## 后续扩展方向

- 增加真实搜索 Agent，对接 Serper、Bing、Tavily 或自定义搜索服务。
- 增加 Outline Agent，把搜索结果整理成板报结构。
- 增加 Writer Agent，生成适合展示的分栏内容。
- 增加前端页面，把生成内容渲染成可分享的 Web 板报。
- 增加导出能力，例如 HTML、Markdown、图片或 PDF。

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

## 感谢与支持

感谢你关注这个项目。信息整理和内容展示看起来朴素，但它正是很多学习、汇报和创作流程里的关键一步。如果这个项目给了你一点启发，欢迎 Star、Fork 或提出建议，你的支持会让我继续把它从一个轻量工作流打磨成更完整、更好用的板报生成工具。
