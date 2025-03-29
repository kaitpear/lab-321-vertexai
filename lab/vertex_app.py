import streamlit as st
import vertexai
import os
from vertexai.generative_models import FunctionDeclaration, GenerationConfig, GenerativeModel, Tool

st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")


# Section A: Add in your Vertex AI API call below

vertexai.init(project=os.environ.get("lab-321-vertexai"), location="us-central1")

model = GenerativeModel(model_name= "gemini-1.5-flash-002", system_instruction= "I want only a bulleted list of the neighboring states you come up with. No other text")

response = model.generate_content(f"Find the neighboring states of {users_state}")

st.write("The neighboring states are:")
st.write(response.text)
