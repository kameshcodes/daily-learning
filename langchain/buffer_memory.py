# Combine Multiple Application

import os 
from constant import OPENAI_API_KEY

from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from langchain.memory import ConversationBufferMemory


import streamlit as st

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

st.title("Celebrity Search Result")
input_text = st.text_input("Search the title you want")

# Buffer Memory 

person_memory =  ConversationBufferMemory(input_key = "name", memory_key="chat_history")
dob_memory =  ConversationBufferMemory(input_key = "person", memory_key="chat_history")
desc_memory =  ConversationBufferMemory(input_key = "person", memory_key="description_history")

# prompt template
first_input_prompt = PromptTemplate(
    input_variables = ["name"],
    template = "Tell me about celebrity {name}"
)

second_input_prompt = PromptTemplate(
    input_variables=["person"],
    template="When was {person} born?."
)

third_input_prompt = PromptTemplate(
    input_variables=["dob"],
    template="Mention 5 Major events happend around {dob} in the world?."
)




if input_text:
    llm = OpenAI(temperature=0.8)
    chain1 = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key="person", memory = person_memory)
    chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key="dob", memory = dob_memory)
    chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key="desc", memory = desc_memory)
    parent_chain = SequentialChain(
        chains=[chain1, chain2, chain3], 
        input_variables=["name"],
        output_variables=["person", "dob", "desc"],
        verbose=True)
    result = parent_chain({"name": input_text})
    st.write(result)
    
    with st.expander("Person Name"):
        st.info(person_memory.buffer)
        
    with st.expander("Major Events"):
        st.info(desc_memory.buffer)