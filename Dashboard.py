import streamlit as st
import pandas as pd
import numpy as np

st.title("Women's Clothing Reviews Dashboard")

#Load Data
@st.cache_data
def load_data(nrows):
    data = pd.read_csv("data_dashboard.csv", nrows=nrows)

    # convert column names to lowercase
    data.columns = data.columns.str.lower()

    # remove unnamed column if it exists
    if "unnamed: 0" in data.columns:
        data = data.rename(columns={"unnamed: 0": "review id"})

    return data


#Loading text
data_load_state = st.text('Loading data...')

data = load_data(10000)

data_load_state.text("Done! (using st.cache_data)")

#Basic info of the dataset
st.subheader("Quick Overview")

st.write("Total rows:", len(data))

# only show these if columns exist (prevents crashes)
if "rating" in data.columns:
    st.write("Average rating:", round(data["rating"].mean(), 2))

#Show raw data 
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)



