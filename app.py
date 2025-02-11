import streamlit as st
from transformers import pipeline

sentiment = pipeline("text-classification")

st.title("Sentiment Analyzer")

user_input = st.text_input("Enter text")

if st.button("Get Sentiment"):
    if user_input:
        result = sentiment(user_input)

        st.write(result[0]['label'])