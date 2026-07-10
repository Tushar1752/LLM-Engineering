"""
Day 19 - Step 1: Your first Streamlit web app.
"""

import streamlit as st
st.title("Hello,Streamlit")
st.header("I am a web page written in python.")
st.subheader("No HTML,No CSS, No JS")
st.write("This whole page is one short Python script")
st.write("Two plus Two is:",2+2)
st.markdown("streamlit understand the **markdown**, so you can *style* text easily. ")
st.button("Click me")
if st.button("Click Here"):
    st.success("You clicked the buttom so streamlit will re ran the whole script")

st.caption("Tip:edit this file,press save and Streamlit will offer to reload the page.")