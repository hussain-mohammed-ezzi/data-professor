# """Python file to serve as the frontend"""
# import streamlit as st
# from streamlit_chat import message

# from langchain.chains import ConversationChain
# from langchain.llms import OpenAI


# def load_chain():
#     """Logic for loading the chain you want to use should go here."""
#     llm = OpenAI(temperature=0, openai_api_key='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')
#     chain = ConversationChain(llm=llm)
#     return chain

# chain = load_chain()



# if "generated" not in st.session_state:
#     st.session_state.generated = []

# if "past" not in st.session_state:
#     st.session_state.cast = []


# def get_text():
#     input_text = st.text_input("You: ", "Hello, how are you?", key="input")
#     return input_text


# user_input = get_text()

# if user_input:
#     output = chain.run(input=user_input)

#     st.session_state.cast.append(user_input)
#     st.session_state.generated.append(output)

# if st.session_state["generated"]:

#     for i in range(len(st.session_state["generated"]) - 1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state.cast[i], is_user=True, key=str(i) + "_user")


import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=(datetime(2020, 1, 1, 9, 30)),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

import pandas as pd
import altair as alt
import numpy as np 
st.header('hawe charts start thai rahyo che')

df3 = pd.DataFrame(np.random.rand(50 , 5 ) , columns = ['a' , 'b' , 'c' , 'd' ,'e'])
c = (alt.Chart(df3).mark_circle().encode(x= 'a' , y= 'b' , size = 'c' , tooltip=['a' , 'b' , 'c' ]) )

st.altair_chart(c , use_container_width=True)


st.header('hawe selectbox shruu thase')

option = st.selectbox('what is you faviourit color' , ('BLue' , 'Green' , 'Red'))
st.write('your favirite color is ' , option )


st.header ('hawe multiselect shruu thaase')
option2 = st.multiselect('select your faviorite colors' , ['Blue' , 'Green' , 'Red', 'White' , 'Sober']  , ['Blue' , 'Green' , ])
st.write('you selected' , option2)


st.header('hawr checkbox start thaase')

import streamlit as st

st.write('what would you like to order')

def sum(a , b):
    return a+b

icecream = st.checkbox('Ice cream' , sum , {'go' , 'jannat'})
cofee = st.checkbox('cofee')
cola = st.checkbox('Cola')

if icecream:
    st.write('great! heres some more')
   
if cofee: 
    st.write('okay here som cofee')
if cola: 
    st.write('here you go')


st.header('hawe componets start thasse')

import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pydantic_settings import BaseSettings

df = pd.read_csv('https://githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
pr = df.profile_report()
st_profile_report(pr)


st.header('hawe latex start thase')

import streamlit as st

st.latex(r'''a+ ar + a r^2'+ ar^3 \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a\left(\frac{1-r^{n}}{1-r)\right''')



