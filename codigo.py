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


user_input = st.sidebar.text_input("Como te llamas?")
if user_input:
  st.sidebar.write('hola',user_input)

with st.sidebar:
    st.write("# Cambiar cantidad de Bins")
    div = st.slider('Número de bins:', 0, 100, 1)
    st.write("Bins =", div)


import numpy as np

# 
def plot_chart(color):
    x = np.arange(10)
    y = np.random.randint(1, 10, size=10)
    plt.bar(x, y, color=color)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    st.pyplot(plt.gcf())


color_options = {
    'Rojo': 'red',
    'Azul': 'blue',
    'Dorado': 'gold',
    'Rosado': 'pink'
}


color_choice = st.selectbox('Cambia el color del gráfico', list(color_options.keys()))


plot_chart(color_options[color_choice])

plt.figure(figsize=(12, 6))
plt.hist(df['Gross Worldwide'], bins=div) 
plt.xlabel('Gross Worldwide)')
plt.ylabel('Budget')
plt.title('Ganancias generadas por marvel y dc')
st.pyplot()


plt.figure(figsize=(12, 6))
plt.hist(df['Company'], bins=div) 
plt.xlabel('Company)')
plt.ylabel('Rate')
plt.title('Quien tiene mejor ratio?')
st.pyplot()


if st.button('no pulses este boton'):
    st.write('no me hiciste caso :|')
else:
    st.write('porfavor no lo presiones')
