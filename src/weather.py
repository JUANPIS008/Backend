import requests

def get_weather(city):
    api_key = '57ecb6256c8659652b23f5e1c7078a92'
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es'
    response = requests.get(base_url)
    return response.json()
