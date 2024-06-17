import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data

st.title("Weather Forecast for the next days.")

place = st.text_input(label="Place:", key="place_textbox")

number_days = st.slider(label="Forecast Days:", min_value=1,
                        max_value=5, key="slider")

data_view = st.selectbox(label="Select data to view:",
                         options=["Temperature", "Sky"])

st.subheader(f"{data_view} for the next {number_days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, number_days)

        if data_view == "Temperature":
            temperatures = [item["main"]["temp"]/10 for item in filtered_data]
            dates = [item["dt_txt"] for item in filtered_data]
            # Create a line graph
            figure = px.line(x=dates,
                             y=temperatures,
                             labels={"x": "Date", "y": "Temperature(C)"})
            # This streamlit widget receives a figure object from plotly
            # library
            st.plotly_chart(figure)
        else:
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [item["weather"][0]["main"]
                              for item in filtered_data]
            images_path = [images[condition] for condition in sky_conditions]
            st.image(images_path, width=115)

    except KeyError:
        st.text("Please enter a existing place!")
