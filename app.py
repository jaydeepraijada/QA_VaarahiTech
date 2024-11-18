import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.document_loaders import WikipediaLoader  # Import for loading Wikipedia articles

# Load environment variables from a .env file
load_dotenv()  # Adjust the path if necessary

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Create a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "You are a helpful assistant. Please respond to the question asked based mostly on the context provided. Context: {context}. If not present in context, say not present in the given context"),
        ("user", "Question: {question}")
    ]
)

st.title("Question and Answering")

# Initialize session state variables if not present
if "input_type" not in st.session_state:
    st.session_state.input_type = "Direct Text Input"
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "context_text" not in st.session_state:
    st.session_state.context_text = ""

# Function to reset session state when switching input type
def reset_inputs():
    st.session_state.input_text = ""
    st.session_state.context_text = ""

# Sidebar for selecting input type with reset callback
input_type = st.sidebar.selectbox(
    'Select Input Type',
    ('Direct Text Input', 'Wikipedia Topic'),
    key="input_type",
    on_change=reset_inputs
)

# Handle input based on the selected type
if input_type == 'Direct Text Input':
    # Direct Text Input Mode
    context_text = st.text_area("Enter your context here:", key="direct_context")
    question = st.text_input(
        "What question do you have in mind?", 
        value=st.session_state.input_text,
        key="direct_question"
    )
    st.session_state.input_text = question
    st.session_state.context_text = context_text
else:
    # Wikipedia Topic Mode
    topic = st.text_input("Enter Wikipedia Topic:", key="wiki_topic")
    if topic:
        # Load the Wikipedia article
        full_content = WikipediaLoader(query=topic, load_max_docs=2).load()
        
        # Limit the content size (e.g., first 1000 characters)
        max_length = 1000
        st.session_state.context_text = full_content[:max_length]  # Truncate to max_length
        if len(full_content) > max_length:
            st.session_state.context_text += "..."  # Indicate that the text has been truncated

    # Ensure the question input starts empty
    question = st.text_input(
        "What question do you have in mind?", 
        value=st.session_state.input_text,
        key="wiki_question"
    )
    st.session_state.input_text = question

# Initialize the OpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo")  # Use OpenAI model
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if st.session_state.input_text:
    # Use context_text if provided, otherwise use the loaded Wikipedia content
    response = chain.invoke({
        "question": st.session_state.input_text, 
        "context": st.session_state.context_text
    })
    st.write(response)
