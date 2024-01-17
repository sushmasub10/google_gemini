from dotenv import load_dotenv
# loading all env variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A demo")
st.header("gemini llm application")
input = st.text_input("input ", key="input")
submit = st.button("ask a question")

# when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)