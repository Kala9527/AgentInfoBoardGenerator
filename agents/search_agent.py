from typing import TypedDict

from langchain_core.prompts import ChatPromptTemplate

from llm import llm
from utils import json_parser


class State(TypedDict):
    require: str
    kw_list: list[str]
    search_result: dict[str, str]


generate_query_kw_list_template = ChatPromptTemplate.from_template(
    """# Background
You are a research editor in a newsroom. The newsroom needs to generate news-search keywords from a short user brief.

# Role
You are responsible for collecting source material. Based on the user requirement, generate multiple search-engine query keywords.

# User requirement
{require}

# Output format
Return only a fenced JSON array:

```json
[
  "query keyword",
  "query keyword",
  "query keyword"
]
```
"""
)

generate_kw_list_chain = generate_query_kw_list_template | llm | json_parser


if __name__ == '__main__':
    result = generate_kw_list_chain.invoke(
        {'require': 'Generate three Chinese search keywords about AI industry investment trends.'}
    )
    print(result)
