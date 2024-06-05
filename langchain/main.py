# Integrate with OPEN API

import os 
from constant import OPENAI_API_KEY

from langchain.llms import OpenAI

import streamlit as st

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

#streamlit framework
st.title("Langchain DEMO with OPENAI API")
input_text = st.text_input("Search the topic you want")


if input_text:
    llm = OpenAI(temperature=0.8)
    st.write(llm(input_text))
    