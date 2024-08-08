import requests


def get_data(place, number_days, kind):
    """
    Fetch weather data for a given place and number of days.

    Args:
        place (str): The name of the place to fetch weather data for.
        number_days (int): The number of days to fetch the forecast for.
        kind (str): The type of data to fetch ("Temperature" or "Sky").

    Returns:
        tuple: A tuple containing two lists - dates and values.
    """
    # API endpoint for fetching weather data
    API_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={number_days * 8}&appid=YOUR_API_KEY"

    # Send a request to the API
    response = requests.get(API_URL)
    data = response.json()

    # Filter the data to get the required information
    filtered_data = data["list"]

    if kind == "Temperature":
        # Extract temperature data
        temp_list = [item["main"]["temp"] / 10 for item in filtered_data]
        dates_list = [item["dt_txt"] for item in filtered_data]
        x_axis = dates_list
        y_axis = temp_list
        return x_axis, y_axis
    else:
        # Extract sky condition data
        sky_list = [item["weather"][0]["main"] for item in filtered_data]
        dates_list = [item["dt_txt"][:10] for item in filtered_data]
        x_axis = dates_list
        y_axis = sky_list
        return x_axis, y_axis
