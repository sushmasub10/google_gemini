import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
# as soon as we read the pdf we should convert them into vectors. 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
# vector embedding
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
# helps to chat and prompts
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# read pdf extract text and return the text. 

def get_pdf_text(pdf_docs):
    text = ""
    # read pdfs
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        # pdf_reader will be in list 
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return text

# convert text into smaller chunks
def get_text_chunks(text):
    # convert the larger text into 100000 words as a single chunk with 1000 words overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    # splitting the text
    chunks = text_splitter.split_text(text)
    return chunks


# convert chuks into vectors

def get_vector_chunks(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "moodels/embeddings-001")
    
