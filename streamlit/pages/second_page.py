import streamlit as st

st.title("Second Page")

st.write("""
         This is the second page of the Streamlit app. The first page is the
         main page. This page is a sub-page that can be accessed from the main
         page. The main page is the first page that is displayed when the app
         is opened.
         """)

left, right = st.columns(2)

with left:
    if st.button('Back', use_container_width=True):
        st.switch_page('hello_snowflake.py')

with right:
    if st.button('Next Page', use_container_width=True):
        st.switch_page('pages/third_page.py')
