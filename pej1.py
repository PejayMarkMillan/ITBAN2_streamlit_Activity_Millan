# app.py
import streamlit as st
import pandas as pd

st.title("CSV Data Filter App")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    st.write("---")

    st.subheader("Filter Data")

    # Let user choose which column to filter
    column = st.selectbox("Choose a column to filter by", df.columns)

    # Let user choose multiple values from that column
    selected_values = st.multiselect(f"Select value(s) from '{column}'", df[column].unique())

    if selected_values:
        filtered_df = df[df[column].isin(selected_values)]
        st.write(f"Filtered Data ({column} in {selected_values}):")
        st.dataframe(filtered_df)
    else:
        st.write("No filter applied.")