import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpeg')

with col2:
    st.title("Farukh Mushtaq")
    content = """
    My career as professional include over 16 years of management and hands-on development experience. Had worked using variety of technologies, tools, languages and architectures. Have introduced successful products at different stages of jobs. Have developed skills, learnt new technologies and adopted best practices which helped me to provide efficient and reliable results.
    """
    st.info(content)
