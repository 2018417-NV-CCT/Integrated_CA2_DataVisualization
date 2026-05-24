import streamlit as st
import pandas as pd
import numpy as np



#st.markdown('<div class="main-title">👗 Women\'s Clothing Reviews Dashboard</div>', #unsafe_allow_html=True)


st.title("👗 Women's Clothing Reviews Dashboard 💅")
st.markdown("---")



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

data_load_state.text("Loading Data Done! 🟩")

st.markdown("---")


#Basic info of the dataset
st.header("Quick Overview")

st.write("Total rows:", len(data))

# only show these if columns exist (prevents crashes)
if "rating" in data.columns:
    st.write("Average rating:", round(data["rating"].mean(), 2))

#Show raw data 
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.markdown("---")

#1-DATA OVERVIEW


#st.header("📊 Dashboard Summary")

st.markdown(
    """
    <div style="
        background-color:#f7a1c4;
        padding:15px;
        border-radius:8px;
        font-weight:700;
        font-size:26px;
        color:#1a1a1a;
    ">
        📊 Dashboard Summary
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Summary of all Customer Reviews:")

col1, col2, col3 = st.columns(3)

col1.metric("Total Reviews", len(data))
col2.metric("Clothing Items", data["clothing id"].nunique())
col3.metric("Average Rating", round(data["rating"].mean(), 2))

st.markdown("---")

#2-RATING DISTRIBUTION

#st.header("⭐ Ratings ")


st.markdown(
    """
    <div style="
        background-color:#a4c2f4;
        padding:15px;
        border-radius:8px;
        font-weight:700;
        font-size:26px;
        color:#1a1a1a;
    ">
        ⭐ Ratings
    </div>
    """,
    unsafe_allow_html=True
)
st.write("This chart shows how customers rated products")

rating_counts = data["rating"].value_counts().sort_index()
st.bar_chart(rating_counts)

st.markdown("---")

#3-AGE DISTRIBUTION

#st.header("👥 Customers Age")


st.markdown(
    """
    <div style="
        background-color:#b6d7a8;
        padding:15px;
        border-radius:8px;
        font-weight:700;
        font-size:26px;
        color:#1a1a1a;
    ">
        👥 Customers Age
    </div>
    """,
    unsafe_allow_html=True
)
age_counts = data["age"].value_counts().sort_index()
st.bar_chart(age_counts)

st.markdown("---")

#4-CLOTHING CATEGORIES

#st.header("👗 Clothing Categories 🧤")


st.markdown(
    """
    <div style="
        background-color:#f9e79f;
        padding:15px;
        border-radius:8px;
        font-weight:700;
        font-size:26px;
        color:#1a1a1a;
    ">
        👗 Clothing Categories
    </div>
    """,
    unsafe_allow_html=True
)
st.write("Clothing types that are most reviewed")
cat_counts = data["class name"].value_counts()
st.bar_chart(cat_counts)

st.markdown("---")

