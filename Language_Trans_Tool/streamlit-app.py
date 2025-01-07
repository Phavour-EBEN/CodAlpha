import streamlit as st
from language_trans import LANGUAGES, get_language_name, run_translation

def main():
    st.set_page_config(page_title="Language Translator", page_icon="🌍")
    
    # Add title and description
    st.title("🌍 Language Translator")
    st.write("Translate text into multiple languages instantly!")

    # Create two columns for input and output
    col1, col2 = st.columns(2)

    with col1:
        # Input text area
        input_text = st.text_area("Enter text to translate:", height=150)
        
        # Language selection dropdown - using the imported LANGUAGES dictionary
        target_language = st.selectbox(
            "Select target language:",
            options=sorted(LANGUAGES.values()),
            index=sorted(LANGUAGES.values()).index('spanish')  # Default to Spanish
        )

        # Translate button
        if st.button("Translate"):
            if input_text:
                with st.spinner("Translating..."):
                    # Get language code and translate using imported functions
                    lang_code = get_language_name(target_language)
                    translated_text = run_translation(input_text, lang_code)
                    
                    # Store the result in session state
                    st.session_state.translated_text = translated_text
            else:
                st.warning("Please enter some text to translate.")

    with col2:
        # Output text area
        st.text_area(
            "Translated text:",
            value=st.session_state.get('translated_text', ''),
            height=150
        )

    # Add footer with information
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Powered by Google Translate API</p>
            <p>Supports 100+ languages</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()