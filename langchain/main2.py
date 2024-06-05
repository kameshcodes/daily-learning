# let do some prompt engineering

import os 
from constant import OPENAI_API_KEY
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

st.title("Celebrity Search Result")
input_text = st.text_input("Search the title you want")

# prompt template
first_input_prompt = PromptTemplate(
    input_variables = ["name"],
    template = "Tell me about celebrity {name}"
)

if input_text:
    llm= OpenAI(temperature = 0.8)
    chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)
    st.write(chain.run(input_text))
    