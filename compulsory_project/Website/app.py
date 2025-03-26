import streamlit as st
import pandas as pd
import matplotlib.pyplot as pyplot

st.title("Simple data")
upload_file = st.file_uploader("choose a CSV file",type="csv")

if upload_file is not None:
    st.write("file uploaded")
    df=  pd.read_csv(upload_file)

    st.subheader("data preview")
    st.write(df.head())

    st.subheader("Data summary")
    st.write(df.describe())

    st.subheader("filter data")
    col = df.columns.tolist()
    select_column = st.selectbox("sleect column to filter",col)

    unique_value =df[select_column].unique()

    select_value = st.selectbox("sleect value",unique_value)

    fliter_df = df[df[select_column] == select_value]

    st.write(fliter_df)

    st.subheader("plot data")
    x_col = st.selectbox("select x-axia col",col)
    y_col = st.selectbox("select y-axia col",col)

    if st.button("Generate plot"):
        st.line_chart(fliter_df.set_index(x_col)[y_col])
else:
    st.write("wating for file to upload")


