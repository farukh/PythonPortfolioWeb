import streamlit as st
st.title("Contact Us")
with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address:")
    message = st.text_area("Your Message: ")
    btn_submit = st.form_submit_button("Submit")
    print(btn_submit)
    if btn_submit:
        print('Button Pressed...')
