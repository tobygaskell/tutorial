# Import python packages
import streamlit as st
from snowflake.snowpark import Session


st.title("Hello Snowflake - Streamlit Edition")

st.write("""
         The following data is from the accounts table in the application
         package. However, the Streamlit app queries this data from a view
         called code_schema.accounts_view.
         """)

session = Session.builder.getOrCreate()

data_frame = session.sql("""
                         SELECT *
                         FROM hello_snowflake_app.code_schema.accounts_view
                         """)

queried_data = data_frame.to_pandas()

st.dataframe(queried_data, use_container_width=True)

if st.button('Next Page', use_container_width=True):
    st.switch_page('pages/second_page.py')
