import streamlit as st

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

st.set_page_config(page_title="Pinecone Settings", layout="wide")

st.title("账号信息")

pinecone_api_key = st.text_input("ID", value=st.session_state["PINECONE_API_KEY"], max_chars=None, key=None, type='default')
environment = st.text_input("秘钥", value=st.session_state["PINECONE_ENVIRONMENT"], max_chars=None, key=None, type='default')

saved = st.button("Save")

if saved:
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"] = environment