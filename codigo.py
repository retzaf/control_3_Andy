import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
db = 'db.csv'
df = pd.read_csv(db,sep = ',')

st.write("""
# Netflix Movies
## Gráficos usando la base de datos
""")
