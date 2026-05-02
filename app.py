import streamlit as st
import pandas as pd

st.title("Supermart Retail Dashboard")

df= pd.read_csv("data.csv")

st.write("Dataset Preview")
st.write(df.head())

st.write("Sales Chart")
st.line_chart(df["Sales"])
