import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
db = 'db.csv'
df = pd.read_csv(db, sep=',', encoding='latin-1') 

st.write("""
# Marvel vs Dc
## Gráficos
""")

st.sidebar.image("")

with st.sidebar:
    st.write("# Opciones")
    div = st.slider('Número de bins:', 0, 10, 2)
    st.write("Bins =", div)

plt.figure(figsize=(12, 6))
plt.hist(df['worldwide gross ($m)'], bins=10) # Using a default of 10 bins
plt.xlabel('worldwide gross ($m)')
plt.ylabel('% budget recovered')
plt.title('Histogram of worldwide gross')
st.pyplot()
