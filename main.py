import streamlit as st
import plotly.express as px
import pandas as pd

st.header("In Search for Happiness")
x_axis = st.selectbox("Select the data for the X-axis",
                      ["GDP", "Happiness", "Generosity"])
y_axis = st.selectbox("Select the data for the Y-axis",
                      ["GDP", "Happiness", "Generosity"])
st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("happiness.csv")

x = df[x_axis.lower()]
y = df[y_axis.lower()]

figure = px.scatter(x=x, y=y, labels={"x": x_axis, "y": y_axis}, )
st.plotly_chart(figure)
