import streamlit as st
from chatbot import get_response

# Page settings
st.set_page_config(page_title="ChatBot", page_icon="💬")
st.title("💬 Simple ChatBot")
st.markdown("Talk to the bot below — like WhatsApp. Type 'bye' to exit.")

# Initialize message history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat display: show all messages
for entry in st.session_state.chat_history:
    sender, msg = entry
    if sender == "user":
        st.markdown(f"<div style='text-align: right; color: white; background-color: #25D366; padding: 8px 12px; border-radius: 12px; margin: 4px 0; display: inline-block; max-width: 70%;'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; color: black; background-color: #E4E6EB; padding: 8px 12px; border-radius: 12px; margin: 4px 0; display: inline-block; max-width: 70%;'>{msg}</div>", unsafe_allow_html=True)

# Input box and submit button
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_message")
    submitted = st.form_submit_button("Send")

# Handle user input
if submitted and user_input:
    # Append user's message
    st.session_state.chat_history.append(("user", user_input))

    # Get bot's response
    response = get_response(user_input)

    # Append bot's reply
    st.session_state.chat_history.append(("bot", response))
