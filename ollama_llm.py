import os
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

llm=ChatOpenAI(
    model='GLM-4-Flash',
    openai_api_key=os.getenv('ZHIPU_API_KEY'),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)