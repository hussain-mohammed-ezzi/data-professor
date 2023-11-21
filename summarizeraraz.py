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


import numpy as np 
import altair as alt
import pandas as pd 
import streamlit as st

st.header('st.write batawi rahy chy joi le ')

st.write('hello *world* : dont look at my new sunglasses')

st.write(1234)

df = pd.DataFrame({'firstcolumn': [1,2,4,5,6],
                  'secondcolumn': [3,4,5,6,6]})
st.write(df)

st.write('belos is a datafram '  , df , 'above is a dataframe')

df2 = pd.DataFrame(np.random.rand(200, 3),
                   
                 columns= ['a' , 'b' , 'c']  )

c = alt.Chart(df2).mark_circle().encode(x='a' , y = 'b' , size = 'c' , color = 'c' , tooltip = ['a' , 'b' , 'c'])
st.write(c)