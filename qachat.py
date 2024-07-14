from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the Generative AI API with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel and start a chat
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    """Function to get a response from the Gemini model."""
    response = chat.send_message(question, stream=True)
    return response

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input text box
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If the button is clicked and input is not empty, get and display the response
if submit and input_text:
    response = get_gemini_response(input_text)
    
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
