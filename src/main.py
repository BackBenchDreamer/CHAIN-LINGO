import streamlit as st
from translator_utils import translate

st.set_page_config(
    page_title="Translator.AI", 
    page_icon="ಆ", 
    layout="centered",
)

st.title("ಆआஆ - Translator Application")

col1, col2 = st.columns(2)

with col1: 
    input_languages_list = ["English", "Hindi", "Kannada", "Tamil", "Telugu"]
    input_language = st.selectbox(label = "Select Input Language", options = input_languages_list)

with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label = "Select Output Language", options = output_languages_list)

input_text = st.text_area("Enter Text to Translate", value = "Hello, World!")  

if st.button("Translate"):
    translated_text = translate(input_language, output_language, input_text)
    st.success(translated_text)