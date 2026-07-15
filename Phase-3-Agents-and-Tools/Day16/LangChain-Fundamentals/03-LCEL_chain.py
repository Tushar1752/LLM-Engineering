"""
03 - LCEL: chaining pieces with the | operator (the core idea of LangChain).

LCEL = "LangChain Expression Language". It's just this: the pipe operator |
feeds the output of the thing on its left into the thing on its right.

    chain = prompt | model | parser

Read it left to right: fill the prompt -> send to the model -> pull clean text
out of the reply. The whole chain is itself a "Runnable" with .invoke(),
.batch(), and .stream().
The | mechanics run offline (we chain two plain Python functions to prove it).
The full prompt|model|parser needs a key.
"""
 

from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
load_dotenv()
MODEL = "llama-3.1-8b-instant"
to_upper = RunnableLambda(lambda s: s.upper())
add_bang = RunnableLambda(lambda s: s + "!")
tiny_chain = to_upper | add_bang
print("tiny_chain.invoke('hello') =>", tiny_chain.invoke("hello"))
print("The | is just data flowing left -> right. That's all LCEL is.")
print()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])
parser = StrOutputParser()
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY found.")
    print("With a key, this runs:")
    print("chain = prompt | model | parser")
    print('chain.invoke({"question": "What is Python?"}) -> plain string')
else:
    model = ChatGroq(
        model=MODEL,
        temperature=0
    )
    chain = prompt | model | parser
    answer = chain.invoke(
        {"question": "What is Python in one line?"}
    )
    print("Invoke ->", answer)
    print()
    questions = [
        {"question": "What is HTML?"},
        {"question": "What is HTTP?"}
    ]
    answers = chain.batch(questions)
    for q, a in zip(questions, answers):
        print(f"Batch -> {q['question']:15} {a}")
    print()
    print("Stream -> ", end="", flush=True)

    for piece in chain.stream(
        {"question": "Name three uses of Python."}
    ):
        print(piece, end="", flush=True)

    print()

print()
print("Every LangChain piece (prompt, model, parser, retriever, tool)")
print("is a Runnable, so they all share invoke(), batch(), and stream().")
print("They all snap together using the | operator.")