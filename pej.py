# app.py
import streamlit as st

st.title("Hello, MILLAN!")
st.header("Welcome to Your First Streamlit App")
st.write("This app demonstrates basic input and output using Streamlit.")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1)
email = st.text_input("Enter your email:")

# Output section
if name and age and email:
    st.write(f"Hello, {name}! You are {int(age)} years old.")
    st.write(f"Your email is: {email}")