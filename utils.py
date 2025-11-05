#通常是工具函数
# hel
import re

from langchain_core.messages import AIMessage
from langchain_core.runnables import chain

json_parse_regex = re.compile('```json(.+)```', re.DOTALL)
html_parse_regex = re.compile('```html(.+)```', re.DOTALL)

def parse_json(json_str):
    match = json_parse_regex.search(json_str)
    # 只有 match 存在才解析 json 数据
    if match:
        json_str = match.groups()[0]
    else:
        print(json_str)
        raise Exception('格式错误')

@chain
def json_parser(ai_message: AIMessage):
    return parse_json(ai_message.content)