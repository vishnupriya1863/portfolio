import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.png")

with col2:
    st.title("Vishnu Priya Muchhintala")
    content = """
    Hi, I am Vishnu Priya Muchhintala! I am a Python programming learner. I'm into 3rd year of my  B.Tech in Computer Science & Engineering in Vidya Jyothi Institute of Technology from the University of Anurag in Hyderabad.
    """
    st.info(content)
    content2 = """
Below are some of the projects that I did :"""
st.write(content2)

col3,empty_col ,col4 = st.columns([1.5,0.5,1.5])
df= pandas.read_csv("data.csv", sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])


