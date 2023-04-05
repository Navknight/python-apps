import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Abhinav Gupta")
    content = '''
    Hi, I am Abhinav! I am a Computer Science and Engineering student from IIT Tirupati.'''
    st.info(content)