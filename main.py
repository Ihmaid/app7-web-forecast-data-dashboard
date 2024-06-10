import streamlit as st

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