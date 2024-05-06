import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Create two columns
col1, col2 = st.columns(2)

# Column 1: Display an image
with col1:
    st.image(r"E:\python_projects\portfolio\photo.png")

# Column 2: Display text content
with col2:
    st.title("Muchhintala Vishnu Priya")
    content = "I'm learning Python currently."
    st.info(content)
    content2 = """ Here are some of the products i built . pls feel free to contact me for any queries"""
    st.write(content2)