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
plt.hist(df['Company'], bins=10) # Using a default of 10 bins
plt.xlabel('Company)')
plt.ylabel('Rate')
plt.title('nose')
st.pyplot()
