"""
Day 19 - Step 5: The rerun model and st.session_state.

This is THE concept of the day. Keep the terminal visible while you click:
you will see one "SCRIPT RAN" line printed for every single interaction, proving
that Streamlit re-runs the entire file top to bottom each time.
"""

import streamlit as st
count = 0
if st.button("Add On"):
    count = count+1
st.write("Count",count)

#st.session_state
if"count" not in st.session_state:
    st.session_state.count=0
if st.button("Add One"):
    st.session_state.count+=1
st.write("Count value:", st.session_state.count)
