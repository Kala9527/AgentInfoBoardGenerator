import json
import re

from langchain_core.messages import AIMessage
from langchain_core.runnables import chain

json_parse_regex = re.compile(r'```json\s*(.+?)\s*```', re.DOTALL)
html_parse_regex = re.compile(r'```html\s*(.+?)\s*```', re.DOTALL)


def parse_json(json_str: str):
    match = json_parse_regex.search(json_str)
    if not match:
        raise ValueError('Expected a fenced json code block in the model response.')

    return json.loads(match.group(1))


@chain
def json_parser(ai_message: AIMessage):
    return parse_json(ai_message.content)
