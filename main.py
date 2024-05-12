import streamlit as st
import pandas
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
content = """Below you can find some of app that I have develop in Python. Feel free to contact me."""
st.write(content)

col3, col4 = st.columns(2)
df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df.iterrows():
        if index % 2 != 0:
            st.header(row['title'])
with col4:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.header(row['title'])
# another way to iterate df rows is to show first 10 rows in col3 by using
# " for index, row in df[:10].iterrows(): " and  col4 show all after 10 using
# " for index, row in df[10:].iterrows():

