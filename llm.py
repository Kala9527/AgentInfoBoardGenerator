import os

from langchain_openai import ChatOpenAI

import load_env  # noqa: F401

llm = ChatOpenAI(
    model='GLM-4-Flash',
    openai_api_key=os.getenv('ZHIPU_API_KEY'),
    openai_api_base='https://open.bigmodel.cn/api/paas/v4/',
)
