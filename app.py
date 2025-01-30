import duckdb
import pandas as pd
import streamlit as st
import io

print("Je printe ça là")

csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''

print("Je printe ça là")

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()

st.header("enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3  = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?"
        , ("Joins", "GroupBy", "Window functions")
        , index=None
        , placeholder="Select a theme"
    )

    st.write("You selected", option)

sql_query = st.text_area(label="Requête SQL")
result = duckdb.sql(sql_query)
st.write(f"Vous avez entré la quéquette : {sql_query}")
st.dataframe(result)

print("Je printe ça là")
