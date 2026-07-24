"""
02 - Binding tools to a model: llm.bind_tools([...]).

Once bound, the model can answer with a TOOL CALL instead of prose. It reads the
schemas from module 02 and decides, on its own, which tool (if any) fits the
question. We just read resp.tool_calls.

With GROQ_API_KEY set, this calls a real model and shows its choices. Without a
key, it prints the exact tool schemas the model WOULD receive -- so you still see
what .bind_tools() does.

Setup:
    pip install langchain langchain-groq python-dotenv
"""


import os
from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def word_count(text: str) -> int:
    """Count how many words are in a piece of text."""
    return len(text.split())


TOOLS = [multiply, word_count]

questions = [
    "What is 78 * 98?",
    "How many words are in 'Hello my name is Tushar'?",
    "Say hello in one word."
]

llm = ChatGroq(
    model=MODEL,
    temperature=0
)

llm_with_tools = llm.bind_tools(TOOLS)

for q in questions:
    print("=" * 60)
    print("Q:", q)

    resp = llm_with_tools.invoke(q)

    if resp.tool_calls:
        for call in resp.tool_calls:
            print(f"Model wants tool: {call['name']}")
            print(f"Args: {call['args']}")
    else:
        print("Answer:", resp.content)