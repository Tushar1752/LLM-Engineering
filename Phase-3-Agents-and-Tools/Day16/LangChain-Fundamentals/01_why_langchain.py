"""
01 - Why LangChain? The same Groq call, wrapped in a common interface.

On Day 9 we called Groq directly with the `groq` client. That works great.
So why add a framework? Because LangChain gives every model provider the SAME
shape: build messages -> `.invoke(messages)` -> get a reply. Swap Groq for
OpenAI/Anthropic/Ollama by changing ONE line, and reuse the same prompts,
chains, parsers, and memory on top.

This file shows the LangChain version of a Day-9 call, side by side in spirit.


    

"""

from dotenv import load_dotenv
import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

MODEL = "llama-3.1-8b-instant"

messages = [
    SystemMessage(content="You are a concise assistant. Answer in one sentence."),
    HumanMessage(content="Explain what an API is.")
]

print("The messages we will send (role -> text):")

for m in messages:
    print(f"[{m.type}] {m.content}")

print()

if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY found.")
    print("Add it to the .env file.")
else:
    model = ChatGroq(
        model=MODEL,
        temperature=0
    )

    reply = model.invoke(messages)

    print("Reply Type :", type(reply).__name__)
    print("Answer     :", reply.content)

    usage = reply.usage_metadata

    if usage:
        print("Tokens :", usage)

print()

print("Why LangChain?")
print('Groq    : model = ChatGroq(model="llama-3.1-8b-instant")')
print('OpenAI  : model = ChatOpenAI(model="gpt-4o-mini")')
print('Ollama  : model = ChatOllama(model="llama3.1")')
print("Everything else remains the same.")