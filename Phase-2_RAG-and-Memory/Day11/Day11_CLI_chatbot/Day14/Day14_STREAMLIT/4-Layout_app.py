import streamlit as st
st.title("Layout a page")
st.sidebar.header("Settings")
model= st.sidebar.selectbox("Model",["llame","OpenAI","Gemini"])
temperature = st.sidebar.slider("Temperature",0.0,1.0,0.2,0.05 )
show_debug = st.sidebar.checkbox("Show Debug Info")
st.write(f"You picked ** {model} ** at temperature **{temperature}**.")
st.header("Welcome to new page")

# --- Columns: things side by side --------------------------------------------
st.header("Columns put things side by side")

col1,col2,col3 = st.columns(3)
with col1:
    st.write("col1 content")
    st.metric("Users",1280,"+120")
with col2:
    st.write("col2 content")
    st.metric("Active Today",342,"-8")
with col3:
    st.write("col3 content")
    st.metric("Signups",57,"+15")

st.divider()

# --- Tabs: switchable sections -----------------------------------------------
st.header("Tabs act like mini pages")
tab_summary,tab_details = st.tabs(["Summary","Details"])
with tab_summary:
    st.write("This is the tab summary")
with tab_details:
    st.write("This is the tab_details")

st.divider

# --- Expander: hide long content ---------------------------------------------
st.header("Expanders hide long or optional content")

with st.expander("Click to see the content "):
    st.code(
        "You are helpfull assistent",
        language = 'text'
    )


# Use the sidebar checkbox to conditionally show debug info - a very common pattern.
if show_debug:
    st.warning("Debug Mode is ON")
    st.json({"model:": model, "temperature:":temperature})