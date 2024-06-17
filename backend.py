import requests

API_KEY = "ffa4cdc31ffe7722690b050388c4ade2"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"][:(forecast_days * 8)]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=5))
