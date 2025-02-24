# pages/8_🤖_AI_Lawbot.py
import streamlit as st
import google.generativeai as genai

# Set up Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

st.title("🤖 AI Lawbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask a legal question:")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response using Gemini
    with st.chat_message("assistant"):
        response = model.generate_content(
            f"You are a legal assistant. Provide clear and concise answers to the following question: {user_input}"
        )
        st.markdown(response.text)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})