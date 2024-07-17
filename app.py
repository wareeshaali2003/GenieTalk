import streamlit as st
import os
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import Markdown


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function to get response from the Gemini model
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

# Input text box
user_input = st.text_input("Input:", key="input")

# Button to submit the question
submit = st.button("submit the question")

# If the button is clicked, get and display the response
if submit:
    if user_input:
        response = get_gemini_response(user_input)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please enter a question.")
