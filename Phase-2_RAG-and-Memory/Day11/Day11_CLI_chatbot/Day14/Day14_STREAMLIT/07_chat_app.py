"""
Day 19 - Step 7: A Groq-powered chat app in the browser.
"""

import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv(Path(__file__).parent / ".env")

# Debug (baad me is line ko hata dena)
print("API KEY:", os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Groq chat", page_icon="💬")


@st.cache_resource
def get_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        st.error("❌ GROQ_API_KEY not found. Please check your .env file.")
        st.stop()

    return Groq(api_key=api_key)


client = get_client()

st.sidebar.header("Settings")

model = st.sidebar.selectbox(
    "Model",
    [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
    ],
)

system_prompt = st.sidebar.text_area(
    "System prompt (the bot's personality)",
    "You are a friendly, concise assistant for Indian students learning to code.",
)

if st.sidebar.button("Clear chat"):
    st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_text = st.chat_input("Type your message and press Enter")

if user_text:
    st.session_state.messages.append(
        {"role": "user", "content": user_text}
    )

    with st.chat_message("user"):
        st.write(user_text)

    with st.chat_message("assistant"):

        message_to_send = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        message_to_send.extend(st.session_state.messages)

        stream = client.chat.completions.create(
            model=model,
            messages=message_to_send,
            temperature=0.4,
            stream=True,
        )

        reply = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in stream
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply,
        }
    )