from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


LANGCHAIN_API_KEY="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"
OPENAI_API_KEY='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'
LANGCHAIN_PROJECT="Chatbot"

# Environment variable call
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")  # Update if different key

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
    # Manually chain the steps
    prompt_message = prompt.format_messages({"question": input_text})
    response = llm(prompt_message)
    output = output_parser.parse(response)
    
    # Display output in Streamlit
    st.write(output)
