import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Collect user input
user_input = "Describe the process of withrdrawing money in ATM if amount is available in account otherwise throw an error"

# Generate Mermaid.js code using GPT-3
prompt = f"Generate Mermaid.js code for a flowchart: {user_input}"
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=200
)
mermaid_code = response.choices[0].text.strip()

# Print the generated Mermaid.js code
print(mermaid_code)
