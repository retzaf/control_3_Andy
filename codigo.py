import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub

# Download latest version
path = kagglehub.dataset_download("gauthamp10/google-playstore-apps")

print("Path to dataset files:", path)
