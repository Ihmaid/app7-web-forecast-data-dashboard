import requests

API_KEY = "ffa4cdc31ffe7722690b050388c4ade2"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"][:(forecast_days * 8) - 1]

    if kind == "Temperature":
        temp_list = [item["main"]["temp"]/10 for item in filtered_data]
        dates_list = [item["dt_txt"] for item in filtered_data]
        x_axis = dates_list
        y_axis = temp_list
        return x_axis, y_axis
    else:
        sky_list = [item["weather"][0]["main"] for item in filtered_data]
        dates_list = [item["dt_txt"][:10] for item in filtered_data]
        x_axis = dates_list
        y_axis = sky_list
        return x_axis, y_axis

    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=5, kind="Temperature"))
