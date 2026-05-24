import streamlit as st
import pandas as pd
import numpy as np

st.title("Women's Clothing Reviews Dashboard")

@st.cache_data
def load_data(nrows):
    data = pd.read_csv("data_dashboard.csv", nrows=nrows)

#converting features names to lowercase
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
