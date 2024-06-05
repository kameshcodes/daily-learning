# Combine Multiple Application

import os 
from constant import OPENAI_API_KEY

from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain


import streamlit as st

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

st.title("Celebrity Search Result")
input_text = st.text_input("Search the title you want")

# prompt template
first_input_prompt = PromptTemplate(
    input_variables = ["name"],
    template = "Tell me about celebrity {name}"
)

second_input_prompt = PromptTemplate(
    input_variables = ["person"],
    template="When was {person} born?."
)


if input_text:
    llm= OpenAI(temperature = 0.8)
    chain1 = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key = "person")
    chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key = "dob")
    parent_chain = SimpleSequentialChain(chains=[chain1, chain2], verbose = True)
    st.write(parent_chain.run(input_text))
    