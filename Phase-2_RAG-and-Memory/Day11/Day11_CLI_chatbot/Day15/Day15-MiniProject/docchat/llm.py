"""
docchat/llm.py - everything about talking to the Groq LLM, in one place.

Kept deliberately free of Streamlit so it stays a plain, testable module. The
UI-specific caching (@st.cache_resource) lives in app.py; here we just build a
client and stream a reply.
"""

import os
from groq import Groq


def make_client():
    if not os.getenv("GROQ_API_KEY"):
        return None
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

def complete_answer(client,model:str,message:list, temperature : float,max_token:int)->str:
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        message=message,
        max_token=max_token,
    )
    return response.choices[0].message.content or ""

def stream_answer(client, model: str, messages: list,temperature: float, max_tokens: int):

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,   
    )
    for chunk in stream:
        piece = chunk.choices[0].delta.content
        if piece:
            yield piece


if __name__=="__main__":
    from dotenv import load_dotenv
    load_dotenv()
    client = make_client()
    if client is None:
        print("NO GROQ_API_KEY set - skipping live test (this is fine).")
    else:
        msg=[{"role":"user", "content":"Say 'llm.py works' and nothing else."}]
        print(complete_answer(client,"llama-3.1-8b-instant", msg,0.0,20))


