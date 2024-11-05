import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("insertar texto")
st.sidebar.header("insertar texto")
st.sidebar.write("insertar texto")

st.sidebar.image("DEFINICIONES-PNG.jpg")
if st.sidebar.button("insertar texto"):
    st.sidebar.write("insertar texto")
 
user_input = st.sidebar.text_input("insertar texto")
st.sidebar.write("insertar texto", user_input)
