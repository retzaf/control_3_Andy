import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
db = 'db.csv'
df = pd.read_csv(db, sep=',', encoding='latin-1') 

st.write("""
# Marvel vs Dc
## Gráficos
""")

with st.sidebar:
    st.write("# Opciones")
    div = st.slider('Número de bins:', 0, 10, 2)
    st.write("Bins =", div)

plt.figure(figsize=(12, 6))
plt.hist(df['Gross Worldwide'], bins=div) 
plt.xlabel('Gross Worldwide)')
plt.ylabel('Rate')
plt.title('Gross Worldwide)
st.pyplot()
