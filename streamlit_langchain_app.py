import streamlit as st
from langchain_library import LangChainApp
import openai

# Set up your OpenAI API key
openai.api_key = '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'

class LangChainApp:
    def analyze_text(self, user_input):
        # Generate Mermaid.js code using GPT-3
        prompt = f"Generate Mermaid.js code for a flowchart: {user_input}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        mermaid_code = response.choices[0].text.strip()
        return mermaid_code

def main():
    st.title("LangChain Application")
@@ -9,7 +24,8 @@ def main():
    user_input = st.text_input("Enter your text:")
    if st.button("Analyze"):
        result = langchain_app.analyze_text(user_input)
        st.write("Analysis Result:", result)
        st.code(result, language="mermaid")

if __name__ == "__main__":
    main()
