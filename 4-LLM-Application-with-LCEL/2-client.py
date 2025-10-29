import requests
import streamlit as st

def get_groq_response(input_text):
    # ✅ Use the actual input_text and set language dynamically if needed
    json_body = {
        "input": {
            "language": "French",
            "text": input_text  # ← Use user input!
        },
        "config": {},
        "kwargs": {}
    }
    
    try:
        response = requests.post("http://127.0.0.1:8001/chain/invoke", json=json_body)
        response.raise_for_status()  # Raise an error for bad status
        result = response.json()
        return result.get("output", "No output received")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit UI
st.title("LLM Application Using LCEL")
input_text = st.text_input("Enter the text you want to convert to French")

if input_text:
    with st.spinner("Translating..."):
        output = get_groq_response(input_text)
    st.write("Translation:", output)