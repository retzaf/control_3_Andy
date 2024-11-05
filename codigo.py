import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('db.csv')

st.write("""
# Netflix Movies
## Gráficos usando la base de datos
""")
