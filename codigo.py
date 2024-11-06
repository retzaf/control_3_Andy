import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

db = 'db.csv'
df = pd.read_csv(db, sep=',', encoding='latin-1') 

st.write("""
# Marvel vs Dc
## Gráficos
""")

st.sidebar.image("Marvel-Vs.-DC.jpg")

user_input = st.sidebar.text_input("¿Cómo te llamas?")
if user_input:
    st.sidebar.write('Hola', user_input)

with st.sidebar:
    st.write("# Cambiar cantidad de Bins")
    div = st.slider('Número de bins:', 0, 100, 1)
    st.write("Bins =", div)

color_input = st.sidebar.multiselect(
    "Elige los colores para los gráficos",
    options=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown'],
    default=['green', 'blue']  
)

plt.figure(figsize=(12, 6))
plt.hist(df['Gross Worldwide'], bins=div, color=color_input[0])
plt.xlabel('Gross Worldwide')
plt.ylabel('Budget')
plt.title('Ganancias generadas por Marvel y DC')
st.pyplot()

plt.figure(figsize=(12, 6))
plt.hist(df['Company'], bins=div, color=color_input[1])
plt.xlabel('Company')
plt.ylabel('Rate')
plt.title('¿Quién tiene mejor ratio?')
st.pyplot()

if st.button('no pulses este boton'):
    st.write('no me hiciste caso :|')
else:
    st.write('porfavor no lo presiones')
