import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a file to be uploaded", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter the Data")
    columns = df.columns.to_list()
    selected_column = st.selectbox("Select column to filter by",columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("select value to filter",unique_values)
    filtered_df = df[df[selected_column]==selected_value]

    st.write(filtered_df)

    st.subheader("Plot Data")
    x_col = st.selectbox("Select x-axis column", columns)
    y_col = st.selectbox("Select y-axis column", columns)

    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_col)[y_col])
        # plt.plot(filtered_df[x_col],filtered_df[y_col])
        # st.pyplot(plt.gcf())

else:
    st.write("Waiting for File...")