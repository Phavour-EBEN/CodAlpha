import streamlit as st
from faq_chatbot import FAQChatbot

def initialize_chatbot():
    """Initialize the chatbot and cache it using streamlit"""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = FAQChatbot('product_faq_dataset.csv')

def initialize_chat_history():
    """Initialize the chat history if it doesn't exist"""
    if 'history' not in st.session_state:
        st.session_state.history = []

def add_message(role, content):
    """Add a message to the chat history"""
    st.session_state.history.append({"role": role, "content": content})

def main():
    st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")
    
    # Initialize chatbot and chat history
    initialize_chatbot()
    initialize_chat_history()
    
    # Page title
    st.title("FAQ Chatbot")
    st.write("Welcome! Ask me anything about our Tech product.")
    
    # Display chat history
    for message in st.session_state.history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Get user input
    user_question = st.chat_input("Ask a question...")
    
    if user_question:
        # Add user message to history
        add_message("user", user_question)
        
        # Get chatbot response
        response = st.session_state.chatbot.find_best_match(user_question)
        
        # Format response
        bot_response = ""
        if response['matched_question']:
            bot_response += f"Similar question: {response['matched_question']}\n\n"
        bot_response += f"Answer: {response['answer']}\n\n"
        bot_response += f"Confidence: {response['confidence']:.2f}"
        
        # Add bot response to history
        add_message("assistant", bot_response)
        
        # Force a rerun to update the chat display
        st.rerun()
    
    # Sidebar with clear chat button
    with st.sidebar:
        if st.button("Clear Chat"):
            st.session_state.history = []
            st.rerun()

if __name__ == "__main__":
    main()