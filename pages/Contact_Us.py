import time

import streamlit as st
from send_email import send_email
st.title("Contact Us")
with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address:")
    raw_message = st.text_area("Your Message: ")
    message = f"""Subject: Email Portfolio App\n

        Sent Following Message: {raw_message}
        From: {user_email}
            """
    btn_submit = st.form_submit_button("Submit")
    print(btn_submit)
    if btn_submit:
        msg = st.info("Please wait... \n Email being sent. ")
        send_email(message)
        msg.info("Email Sent Successfully. ")
