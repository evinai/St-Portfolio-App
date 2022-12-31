import streamlit as st


st.set_page_config(layout='wide')

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/1.png")

with col2:
    st.title("Togai Tunca")
    content = """
    I am a Python programmer, teacher, founder of PythonNow. I am a self taught programmer.
    """
    st.info(content)
content2 = """
Below you can find some of the apps I have built in Python. feel free to contact me.
"""
st.write(content2)