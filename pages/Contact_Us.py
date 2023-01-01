import streamlit as st


st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Text")

    button = st.form_submit_button("Submit")
    if button:
        print("I was pressed")