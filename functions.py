import requests

def api_data(lat, long):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return 404
    except requests.exceptions.RequestException:
        return 400