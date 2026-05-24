import streamlit as st
import pandas as pd
import numpy as np

st.title("Women's Clothing Reviews Dashboard")

@st.cache_data
def load_data(nrows):
    data = pd.read_csv("data_dashboard.csv", nrows=nrows)

# drop unnamed column safely
    #data = data.loc[:, ~data.columns.str.contains("^Unnamed")]

    # convert column names to lowercase
    #data.columns = data.columns.str.lower()


#converting features names to lowercase
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data = data.rename(columns={"unnamed: 0": "review id"})
    return data

#adding text
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
