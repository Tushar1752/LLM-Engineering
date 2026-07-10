"""
Day 19 - Step 2: Every common way to put content on a Streamlit page.
"""
import streamlit as st
import pandas as pd
st.title("Way to show content")
st.header("1.Text")
st.write("st.write prints plain text and understand **Markdown** too.")
st.code("def greet(name):\n return f'Hi{name}'", language = 'python' )
st.divider()
students=pd.DataFrame(
    {
        "Name":["Arjit","Ayush","Akash"],
        "City":["Lko" , "Delhi", "Jaipur"],
        "Score":[88,45,67],
    }
)
st.dataframe(students,width="stretch")
st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error")