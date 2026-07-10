import time
import streamlit as st
st.title("Caching: run slow work once ,not every return")

def slow_uncached(n):
    time.sleep(2)
    return n*n

@st.cache_date
def slow_cached(n):
    time.sleep(2)
    return n*n
st.header("Uncached: slow every single time")
number1 = st.slider("Pick a number(uncached)", 1,10,3)
if st.button("Square it (cached)"):
    result=slow_cached(number2)
    st.success(f"{number2} squared is {result}")

st.divider();
st.header("The pattern you will actually use")
number2=st.slider("Picl a number (cached)", 1,10,3)
if st.button("Square it (cached)"):
    result = slow_cached(number2)
    st.success(f"{number2} squared is {result}")

st.caption(
    "Try clicking 'cached' with the same number twice: the second click is instant. "
    "Then change the number and click again: slow once more (a new cache entry)."
)

st.divider()
