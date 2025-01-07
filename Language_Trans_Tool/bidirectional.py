import streamlit as st
from language_trans import LANGUAGES
from googletrans import Translator
import asyncio
import nest_asyncio

# Apply nest_asyncio
nest_asyncio.apply()

async def translate_text(text, source_lang, target_lang):
    """Translate text between any two languages"""
    if not text:
        return ""
        
    translator = Translator()
    
    try:
        translated = await translator.translate(text, src=source_lang, dest=target_lang)
        return translated.text
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return ""

def run_translation(text, source_lang, target_lang):
    """Run translation in event loop"""
    return asyncio.run(translate_text(text, source_lang, target_lang))

def get_language_code(language_name):
    """Get language code from language name"""
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None

def main():
    st.set_page_config(page_title="Language Translator", page_icon="🌍")
    
    # Add title and description
    st.title("🌍 Language Translator")
    st.write("Translate between any two languages!")

    # Create two columns for language selection
    lang_col1, lang_col2 = st.columns(2)
    
    with lang_col1:
        source_language = st.selectbox(
            "From:",
            options=sorted(LANGUAGES.values()),
            index=sorted(LANGUAGES.values()).index('english')  # Default to English
        )

    with lang_col2:
        target_language = st.selectbox(
            "To:",
            options=sorted(LANGUAGES.values()),
            index=sorted(LANGUAGES.values()).index('spanish')  # Default to Spanish
        )

    # Swap languages button
    if st.button("🔄 Swap Languages"):
        # Store current selections
        temp_source = source_language
        temp_target = target_language
        
        # Update session state to swap languages
        st.session_state.source_language = temp_target
        st.session_state.target_language = temp_source
        st.rerun()

    # Create two columns for input and output
    col1, col2 = st.columns(2)

    with col1:
        # Input text area
        input_text = st.text_area(
            f"Enter text in {source_language}:", 
            height=150,
            key="input_text"
        )

    with col2:
        # Output text area
        st.text_area(
            f"Translation in {target_language}:",
            value=st.session_state.get('translated_text', ''),
            height=150,
            key="output_text"
        )

    # Center the translate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Translate button
        if st.button("🔄 Translate", use_container_width=True):
            if input_text:
                with st.spinner("Translating..."):
                    # Get language codes
                    source_code = get_language_code(source_language)
                    target_code = get_language_code(target_language)
                    
                    # Perform translation
                    translated_text = run_translation(input_text, source_code, target_code)
                    
                    # Store the result in session state
                    st.session_state.translated_text = translated_text
            else:
                st.warning("Please enter some text to translate.")

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