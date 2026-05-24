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

data = load_data(23486)

data_load_state.text("Loading Data Done!")

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



#1-DATA OVERVIEW

st.subheader("📊 Dataset Overview")

st.write("Quick summary of the dataset:")

col1, col2, col3 = st.columns(3)

col1.metric("Total Reviews", len(data))
col2.metric("Clothing Items", data["clothing id"].nunique())
col3.metric("Average Rating", round(data["rating"].mean(), 2))



#2-RATING DISTRIBUTION

st.subheader("⭐ Ratings")
rating_counts = data["rating"].value_counts().sort_index()
st.bar_chart(rating_counts)



#-3AGE DISTRIBUTION

st.subheader("👥 Customers Age")
age_counts = data["age"].value_counts().sort_index()
st.bar_chart(age_counts)


#4-CLOTHING CATEGORIES

st.subheader("👗🧤 Clothing Categories")
cat_counts = data["class name"].value_counts()
st.bar_chart(cat_counts)

