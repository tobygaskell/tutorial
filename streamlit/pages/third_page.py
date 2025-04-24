import streamlit as st

st.title("Third Page")

if st.button('Click for Fun!', use_container_width=True):
    st.balloons()

if st.button('Back', use_container_width=True):
    st.switch_page('pages/second_page.py')
