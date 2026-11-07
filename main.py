

import streamlit as st
from dotenv import load_dotenv
#from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq

load_dotenv(verbose=True)

st.set_page_config(
    page_title="💬ChatGroq",
    page_icon="",
    layout="centered",

)

st.title("💬Generative AI Chat")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm  = ChatGroq(
   # model="gemma2:9b",
    model = "openai/gpt-oss-120b",
    temperature= 0
)
user_prompt = st.chat_input("Ask me something")


if  user_prompt:
    st.chat_message('user').markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response = llm.invoke(
        input=[{"role":"user","content":"you are a helpful assistant"},*st.session_state.chat_history]
    )

    assistant_response = response.content

    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)




print("All packages imported successfully")
