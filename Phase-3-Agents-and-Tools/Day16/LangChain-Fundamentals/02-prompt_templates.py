"""
02 - Prompt templates: reusable prompts with fill-in-the-blanks.

Hand-writing the whole message list every time is repetitive and error-prone.
A ChatPromptTemplate is a prompt with {placeholders} you fill in later. Write
the wording once; feed it different values forever.

Most of this file runs WITHOUT a key: turning a template + values into finished
messages is pure local work (no network). We only need Groq for the last part.

"""

from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
load_dotenv()
MODEL = "llama-3.1-8b-instant"
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a translator. Translate the next text into {language}. Reply with only the translation."
    ),
    (
        "human",
        "{text}"
    )
])

print("Template variables it expects:", prompt.input_variables)
print()
messages = prompt.format_messages(
    language="French",
    text="Good morning, friends"
)
print('After filling language="French", text="Good morning, friends":')
for m in messages:
    print(f"[{m.type}] {m.content}")
print()
try:
    prompt.format_messages(language="German")
except KeyError as e:
    print("Missing variable:", e)

print()

# Call Groq
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY found.")
else:
    model = ChatGroq(
        model=MODEL,
        temperature=0
    )
    reply = model.invoke(messages)
    print("Model Translation:", reply.content)