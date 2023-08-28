
import streamlit as st
import openai
import base64
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback

#llm_model = OpenAI(temperature=0.9)

# Set up your OpenAI API key
openai.api_key = os.env.["OPEN_AI_KEY"]

# Prompt templates


class LangChainApp:
    try:
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
    except openai.error.OpenAIError as e:
        st.error("Error generating steps: " + str(e))
# Collect user input
user_input = "Describe the process of withrdrawing money in ATM if amount is available in account otherwise throw an error"

def main():
    st.title("LangChain Application")
    langchain_app = LangChainApp()

    # Streamlit UI elements
    user_input = st.text_input("Enter your text:")
    if st.button("Analyze"):
        result = langchain_app.analyze_text(user_input)
        #st.code(result, language="mermaid")
        st.text(result)
        start_index = result.index("graph")
        extracted_content = result[start_index:]
        graphbytes = extracted_content.encode("ascii")
        base64_bytes = base64.b64encode(graphbytes)
        base64_string = base64_bytes.decode("ascii")
        st.image("https://mermaid.ink/img/" + base64_string)
     

if __name__ == "__main__":
    main()

    # Streamlit UI elements
    user_input = st.text_input("Enter your text:")
    if st.button("Analyze"):
        result = langchain_app.analyze_text(user_input)
        st.code(result, language="mermaid")

if __name__ == "__main__":
    main()
