import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Abhinav Gupta")
    content = '''Hi, I am Abhinav! I am a Computer Science and Engineering student from IIT Tirupati.'''
    st.info(content)

content2 = '''
Below you can find some of the apps I have built in Python. Feel free to check them out'''

st.write(content2)

col3, col4 = st.columns(2)
df = pandas.read_csv("images/data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])