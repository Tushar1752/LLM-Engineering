"""
Day 19 - Step 3: Widgets - the controls the user interacts with.

The big idea: a widget function RETURNS the user's current value. You just use
that value like a normal variable.

"""
import streamlit as st
st.title("Widget: Input you can read")
st.header("Tell me about yourself!!")
name = st.text_input("What is your name?","")
#`st.slider` returns the current slider position. Args: label, min, max, default.
age= st.slider("How old are you?",0,100,20)
# `st.selectbox` returns the option the user picked from a dropdown.
city = st.selectbox("which city", ["Delhi","Mumbai","Lucknow","Pune"])

# `st.checkbox` returns True when ticked, False when not.
subscribed = st.checkbox("Send me updates")

# Because widgets just return values, we can use them immediately.
# `name or 'friend'` falls back to 'friend' while the box is still empty.
st.write(f"Hi ** {name or 'friend'}**, age :{age}, city={city}")


st.divider()

st.header("Live tip calculator")
bill= st.number_input("Bill Amount (Rs)", min_value = 0.00, value=500.00, step=50.00)
tip_percent =st.slider("Tip %", 0,30,10)
tip = bill * tip_percent/100
total = bill+tip
st.metric("Total to pay is:", f"Rs {total:.2f}")
st.write(f" Tip Amount is:{tip:.2f}")
st.divider()