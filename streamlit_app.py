from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API keys from environment or default to hardcoded values (as fallback)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_fallback_openai_key")
LANGCHAIN_API_KEY = os.getenv("sv2_pt_967390b44a504849bd2567ac167c812b_2a9aaaa1cb", "your_fallback_langchain_key")

# Set the environment variables (double-check they aren't None)
if OPENAI_API_KEY and LANGCHAIN_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
else:
    st.error("API keys not found. Make sure the .env file is properly configured.")

# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Create chatbot prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("System", "You are a helpful assistant. Please provide a response to the user's queries."),
        ("User", "Question: {question}")
    ]
)

# Streamlit framework
st.title("Langchain Demo with Open AI API")
input_text = st.text_input("Search the topic you want")

# OpenAI LLM call
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

# Chain call manually
if input_text:
    try:
        # Manually chain the steps
        prompt_message = prompt.format_messages({"question": input_text})
        response = llm(prompt_message)
        output = output_parser.parse(response)
        
        # Display output in Streamlit
        st.write(output)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
