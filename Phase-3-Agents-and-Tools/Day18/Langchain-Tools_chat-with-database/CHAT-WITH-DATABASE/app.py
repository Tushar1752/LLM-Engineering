import os
from dotenv import load_dotenv
import streamlit as st

import db
from agent import answer_question, build_model

load_dotenv()

st.set_page_config(page_title="Chat With Your Database", page_icon=":bar_chart:")
st.title(":bar_chart: Chat With Your Database")
st.caption("Ask questions in plain English. A Groq model writes and runs the SQL for you.")

if not os.path.exists(db.DB_PATH):
    st.error("store.db not found. Run `python build_sample_db.py` in this folder first.")
    st.stop()

with st.sidebar:
    st.header("Database")
    for table in db.list_tables():
        with st.expander(table):
            st.code(db.get_schema(table), language="text")
    st.caption("Read-only. The agent can only run SELECT queries.")

if not os.getenv("GROQ_API_KEY"):
    st.warning("Set GROQ_API_KEY in a .env file to chat. "
               "The schema on the left comes straight from the database (no key needed).")
    st.stop()


@st.cache_resource
def get_model():
    return build_model()

model = get_model()git 

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("steps"):
            with st.expander("How I got this (tool calls)"):
                for name, args, result in msg["steps"]:
                    st.markdown(f"**{name}**  `{args}`")
                    st.code(result, language="text")

# TODO: complete this block.
if question := st.chat_input("e.g. Which city has the most customers?"):
    st.info("TODO: build the chat handler -- see the comments in app.py.")
    st.session_state.messages.append({"role":"user","content":question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        answer=answer_question(model,question)
        st.markdown(answer)
    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )
