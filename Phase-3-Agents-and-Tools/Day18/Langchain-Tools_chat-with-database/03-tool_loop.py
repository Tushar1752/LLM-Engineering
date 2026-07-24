"""
03 - The tool-calling loop: run the tool, hand the result back, finish.

This is the whole engine of an agent, in ~10 lines:

    messages = [HumanMessage(question)]
    while True:
        ai = model.invoke(messages)          # model's turn
        messages.append(ai)
        if not ai.tool_calls: break          # no tool -> final answer
        for call in ai.tool_calls:           # run each requested tool
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            messages.append(ToolMessage(result, tool_call_id=call["id"]))

With GROQ_API_KEY set, a real model drives the loop. Without a key, an offline
STAND-IN model emits a canned tool call so you still see the exact mechanics.

Setup:
    pip install langchain langchain-groq python-dotenv
"""

import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

load_dotenv()

MODEL = "llama-3.1-8b-instant"


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the exact result."""
    return a + b


@tool
def word_count(text: str) -> int:
    """Count how many words are in a piece of text."""
    return len(text.split())


TOOLS = [multiply, add, word_count]
TOOL_MAP = {t.name: t for t in TOOLS}


def run_loop(model, question):
    messages = [HumanMessage(content=question)]
    step = 0

    while True:
        step += 1

        ai = model.invoke(messages)
        messages.append(ai)

        if not ai.tool_calls:
            print(f"[Step {step}] Model gave the final answer.")
            return ai.content

        for call in ai.tool_calls:
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            print(f"[Step {step}] Ran {call['name']}({call['args']}) -> {result}")

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=call["id"],
                )
            )


class OfflineToolModel:
    def invoke(self, messages):
        already_used_a_tool = any(
            isinstance(m, ToolMessage) for m in messages
        )

        if not already_used_a_tool:
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "multiply",
                        "args": {"a": 6, "b": 7},
                        "id": "call_offline_1",
                    }
                ],
            )

        last_result = [
            m for m in messages if isinstance(m, ToolMessage)
        ][-1].content

        return AIMessage(content=f"The answer is {last_result}.")


if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq

    model = ChatGroq(
        model=MODEL,
        temperature=0,
    ).bind_tools(TOOLS)

    question = "What is 6 times 7, then add 100 to that?"
    print("Using real Groq model.")
    print("Q:", question)

else:
    model = OfflineToolModel()
    question = "What is 6 times 7?"
    print("No GROQ_API_KEY found. Using Offline Tool Model.")
    print("Q:", question)

answer = run_loop(model, question)
print("\nFinal Answer:", answer)
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

load_dotenv()

MODEL = "llama-3.1-8b-instant"


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the exact result."""
    return a + b


@tool
def word_count(text: str) -> int:
    """Count how many words are in a piece of text."""
    return len(text.split())


TOOLS = [multiply, add, word_count]
TOOL_MAP = {t.name: t for t in TOOLS}


def run_loop(model, question):
    messages = [HumanMessage(content=question)]
    step = 0

    while True:
        step += 1

        ai = model.invoke(messages)
        messages.append(ai)

        if not ai.tool_calls:
            print(f"[Step {step}] Model gave the final answer.")
            return ai.content

        for call in ai.tool_calls:
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            print(f"[Step {step}] Ran {call['name']}({call['args']}) -> {result}")

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=call["id"],
                )
            )


class OfflineToolModel:
    def invoke(self, messages):
        already_used_a_tool = any(
            isinstance(m, ToolMessage) for m in messages
        )

        if not already_used_a_tool:
            return AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "multiply",
                        "args": {"a": 6, "b": 7},
                        "id": "call_offline_1",
                    }
                ],
            )

        last_result = [
            m for m in messages if isinstance(m, ToolMessage)
        ][-1].content

        return AIMessage(content=f"The answer is {last_result}.")


if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq

    model = ChatGroq(
        model=MODEL,
        temperature=0,
    ).bind_tools(TOOLS)

    question = "What is 6 times 7, then add 100 to that?"
    print("Using real Groq model.")
    print("Q:", question)

else:
    model = OfflineToolModel()
    question = "What is 6 times 7?"
    print("No GROQ_API_KEY found. Using Offline Tool Model.")
    print("Q:", question)

answer = run_loop(model, question)
print("\nFinal Answer:", answer)