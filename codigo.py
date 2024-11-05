import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

st.write(Netflix Movies)
