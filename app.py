import duckdb
import pandas as pd
import streamlit as st
import io

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


answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""


