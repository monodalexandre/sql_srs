import duckdb
import pandas as pd
import streamlit as st

st.write("hello world")
data = {"a": [1,2,3], "b":[4,5,6]}
df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["cat", "dog"])

with tab1:

    sql_query = st.text_area(label="Requête SQL")
    result = duckdb.sql(sql_query)
    st.write(f"Vous avez entré la quéquette : {sql_query}")
    st.dataframe(result)