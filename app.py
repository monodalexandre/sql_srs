import duckdb
import pandas as pd
import streamlit as st

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?"
        , ("Joins", "GroupBy", "Window functions")
        , index=None
        , placeholder="Select a theme"
    )

    st.write("You selected", option)

data = {"a": [1,2,3], "b":[4,5,6]}
df = pd.DataFrame(data)


sql_query = st.text_area(label="Requête SQL")
result = duckdb.sql(sql_query)
st.write(f"Vous avez entré la quéquette : {sql_query}")
st.dataframe(result)