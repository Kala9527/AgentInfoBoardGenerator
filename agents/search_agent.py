from langchain_core.prompts import ChatPromptTemplate

import load_env
import os
from typing import TypedDict
from ollama_llm import llm
class State(TypedDict):
    require:str

    kw_list:list[str]

    search_result:dict[str,str]

generate_query_kw_list_template = ChatPromptTemplate.from_template("""# 背景
你是新闻编辑部的一员，你们编辑部需要根据用户的一句话需求来生成新闻稿
# 你的角色
你是负责搜索资料的成员，你需要根据用户提供的需求，生成查询关键字
# 你要做什么
你需要根据 `用户需求`，拟定多个搜索引擎用的查询关键字
# 用户需求
{require}
# 输出格式
请输出 json 格式的数据，数据结构如下:

```json
[
    "查询关键字1",
    "查询关键字2",
    "查询关键字3",
    ...
]
```

输出必须以 "```json" 开头，以 "```" 结尾
""")
generate_kw_list_chain = generate_query_kw_list_template | llm | json_parser