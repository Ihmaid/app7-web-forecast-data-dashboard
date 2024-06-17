import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data

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

x_axis, y_axis = get_data(place, number_days, data_view)

# Create a line graph
figure = px.line(x=x_axis,
                 y=y_axis,
                 labels={"x": "Date", "y": "Temperature(C)"})
# This streamlit widget receives a figure object from plotly library
st.plotly_chart(figure)
