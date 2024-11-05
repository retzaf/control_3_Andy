import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("Mi primera barra lateral de streamlit")
st.sidebar.header("Hola barra lateral")
st.sidebar.write("esto es una barra lateral")

st.sidebar.image("images.jpg")
if st.sidebar.button("Presiona aquí"):
    st.sidebar.write("Has presionado el botón")

user_input = st.sidebar.text_input("Escribe tu nombre")
st.sidebar.write("Hola", user_input)
