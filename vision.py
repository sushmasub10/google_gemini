
from dotenv import load_dotenv
# loading all env variables
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

os.getenv("GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if image!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

   

st.set_page_config(page_title="gemini image demo")
st.header("Gemini image application")
input = st.text_input("Input prompt: ", key="input")
uploaded_file = st.file_uploader("choose an image...", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="uploaded image.", use_column_width=True)

submit =st.button("tell me about the image")

if submit :
    response = get_gemini_response(input, image)
    st.subheader("the response is")
    st.write(response)