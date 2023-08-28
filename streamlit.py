
import streamlit as st
import openai
import secrets
import base64
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback
import time 
import logging

#llm_model = OpenAI(temperature=0.9)

# Set up your OpenAI API key
openai.api_key = os.env.["OPEN_AI_KEY"]

# Set up logging
logging.basicConfig(level=logging.INFO)  # Adjust the logging level as needed





class LangChainApp:
    def analyze_text(self, user_input):
        # Generate Mermaid.js code using GPT-3
        prompt = f"Generate Mermaid.js code for a flowchart: {user_input}"
        # Log the prompt
        logging.info("Prompt: %s", prompt)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        mermaid_code = response.choices[0].text.strip()
        return mermaid_code
    
# Collect user input
user_input = "Describe the process of withrdrawing money in ATM if amount is available in account otherwise throw an error"

def main():
    st.title("LangChain Application")
    langchain_app = LangChainApp()

    # Streamlit UI elements
    start_time = time.time()
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
        end_time = time.time()  # Record the end time
        time_taken = end_time - start_time  # Calculate time taken
        logging.info("time taken"+str(time_taken))

if __name__ == "__main__":
    main()
