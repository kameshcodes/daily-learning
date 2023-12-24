import streamlit as st
import pandas as pd

st.markdown("""
            <style>
            .st-emotion-cache-ztfqz8.ef3psqc5
            {
                visibility:hidden;
            }
            .st-emotion-cache-czk5ss.e16jpq800
            {
                visibility:hidden;
            }
            </style>
            """, unsafe_allow_html=True)
# Text Methods 
st.title("Hi, I am streamlit web app title.")
st.header("Hi, I am header.")
st.subheader("Hi, I am subheader.")
st.text("Hi, I am text body. You can use me to create a paragraph.")
st.markdown("**HELLO** World!, *How are you*")
st.markdown("---")
st.markdown("[Google](https://www.google.com)")
st.caption("hi, I am caption")
st.markdown("---")
st.latex(r"\begin{pmatrix}a & b \\ c & d\end{pmatrix}") #use r before latext text
st.markdown("---")
json_dict = {"a":"1,2,3", "b":"1,2,3"}
st.json(json_dict)
st.markdown("---")
code = """
print("Hello World)
def func():
    return 0
"""
st.code(code, language="python")
st.markdown("---")

#Swizz army knife 
st.write("## h2")

#metric function [label, value, delta]
st.metric(label = "windspeed", value="120ms⁻¹", delta = "-1.4ms⁻¹")

st.markdown("---")

tabel = pd.DataFrame({
    "Col1":[1,2,3,4,5],
    "Col2":[3,4,5,6,7]
})

st.table(tabel)
st.dataframe(tabel)

st.markdown("---")
st.title("Image and Videos")
st.markdown("---")

st.image("priya.png", caption="Priya", width=240)
st.audio("onelove.mp3")
#st.video()

st.markdown("---")
st.title("Interactive widgets")
st.markdown("---")

# checkbox
def change():
    print(st.session_state.checker)
state = st.checkbox(label="Checkbox", value=True, on_change=change, key="checker")
if state:
    st.write("Hi")
else:
    pass

#radio
radio_btn = st.radio("In which country you live?", options=("US", "UK", "Canda"))
print(radio_btn)

def button_click():
    print("Button Clicked")
btn = st.button("Click Me!", on_click=button_click)

select = st.selectbox("What is your favoriate car ?", options = ("BMW", "Tesla", "Benz"))
print(select)

mult = st.multiselect("What are your fav brands", options = ("BMW", "Tesla", "Benz"))
st.write(mult)


st.markdown("---")
st.title("Upload Files")
st.markdown("---")

img = st.file_uploader("Please upload an Image", type=['jpg', 'png','jpeg'], accept_multiple_files=True)
if img:
    for i in img:
        st.image(img)
        
        
st.markdown("---")
st.title("More Interactive Widget")
st.markdown("---")

sl = st.slider("This is a slider", value = 30)
st.write(sl)

st.markdown("---")
val = st.text_input("Enter you course title :", max_chars=60)
st.write(val)

val = st.text_area("Enter you course title :", max_chars=60)
st.write(val)

date = st.date_input("Enter You Birthday: ")
#time = st.time_input("Enter Time:")

st.markdown("---")

import time as ts
from datetime import time  

def convert_time(value):
    m,s,ms = value.split(":")
    ts = int(m)*60+int(s)+int(ms)/1000
    return ts

bar = st.progress(0)

time = st.time_input("Set Timer", value=time(0,0,0))
if str(time)=="00:00:00":
    st.write("Please Set Timer")
else:
    sec = convert_time(str(time))
    bar = st.progress(0)
    perc = sec/100
    for i in range(100):
        bar.progress(i+1)
        ts.sleep(perc)
        
st.markdown("---")


st.header("User Registration Form")
#method 1


form = st.form("Form 1")
form.text_input("First Name:")
form.form_submit_button("Submit")

#method 2
with st.form("Form 2"):
    st.text_input("Last_Name")
    st.form_submit_button("Submit")


with st.form("Form 3"):
    col1, col2 = st.columns(2)
    col1.text_input("Firsst_Name")
    col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Pasword")
    st.form_submit_button("Submit")
    
st.write("From 3")



st.markdown("---")

# side bars 
st.sidebar.write("Hello, This is my side bar !")
