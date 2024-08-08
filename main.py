import streamlit as st
import plotly.express as px
from backend import get_data

# Set the title of the Streamlit app
st.title("Weather Forecast for the next days.")

# Input field for the user to enter the place
place = st.text_input(label="Place:", key="place_textbox")

# Slider for the user to select the number of forecast days
number_days = st.slider(label="Forecast Days:", min_value=1,
                        max_value=5, key="slider")

# Dropdown for the user to select the type of data to view
data_view = st.selectbox(label="Select data to view:",
                         options=["Temperature", "Sky"])

# Display a subheader with the selected data view and place
st.subheader(f"{data_view} for the next {number_days} days in {place}")

# Check if a place has been entered
if place:
    try:
        # Get the dates and values from the backend function
        dates, values = get_data(place, number_days, data_view)

        if data_view == "Temperature":
            # Create a line graph for temperature data
            figure = px.line(x=dates,
                             y=values,
                             labels={"x": "Date", "y": "Temperature(C)"})
            # Display the line graph using Streamlit
            st.plotly_chart(figure)
        else:
            # Dictionary mapping weather conditions to image paths
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            # Get the image paths for the sky conditions
            images_path = [images[condition] for condition in values]
            # Display the images using Streamlit
            st.image(images_path, width=115)

    except KeyError:
        # Display an error message if the place is not found
        st.text("Please enter a existing place!")
