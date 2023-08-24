import streamlit as st
from langchain_library import LangChainApp

def main():
    st.title("LangChain Application")
    langchain_app = LangChainApp()

    # Streamlit UI elements
    user_input = st.text_input("Enter your text:")
    if st.button("Analyze"):
        result = langchain_app.analyze_text(user_input)
        st.write("Analysis Result:", result)

if __name__ == "__main__":
    main()
