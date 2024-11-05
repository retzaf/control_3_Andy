import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
db = 'db.csv'
df = pd.read_csv(db, sep=',', encoding='latin-1') 

st.write("""
# Marvel vs Dc
## Gráfico de ganancias
""")

st.sidebar.image("Marvel-Vs.-DC.jpg")

user_input = st.sidebar.text_input("Como te llamas?")
if user_input:
  st.sidebar.write('hola',user_input)
  
                 
with st.sidebar:
    st.write("# Cambiar cantidad de Bins")
    div = st.slider('Número de bins:', 0, 100, 1)
    st.write("Bins =", div)

plt.figure(figsize=(12, 6))
plt.hist(df['Gross Worldwide'], bins=div) 
plt.xlabel('Gross Worldwide)')
plt.ylabel('Budget')
plt.title('Ganancias en el mundo')
st.pyplot()

plt.figure(figsize=(12, 6))
plt.hist(df['Marvel'], bins=div) 
plt.xlabel('Marvel)')
plt.ylabel('Budget')
plt.title('Ganancias en el mundo')
st.pyplot()
