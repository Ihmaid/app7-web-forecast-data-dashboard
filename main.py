import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Weather Forecast for the next days.")

place = st.text_input(label="Place:", key="place_textbox")

number_days = st.slider(label="Forecast Days:", min_value=1,
                        max_value=5, key="slider")

data_view = st.selectbox(label="Select data to view:",
                         options=["Temperature", "Sky"],
                         placeholder=" ",
                         index=None)

if data_view:
    st.subheader(f"{data_view} for the next {number_days} days in {place}")


def get_data(number_days):
    dates = ["2022-10-25", "2022-10-30", "2022-11-05"]
    temperatures = [20, 23, 27]
    temperatures = [number_days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(number_days)

# Create a line graph
figure = px.line(x=d,
                 y=t,
                 labels={"x": "Date", "y": "Temperature(C)"})
# This streamlit widget receives a figure object from plotly library
st.plotly_chart(figure)
