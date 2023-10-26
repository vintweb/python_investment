"""Weather API"""

import api_key
import api_url
import api_view
import requests

api_key = api_key.set_api()

user_input = input('Введите город: ')

weather_data = requests.get(f'{api_url.set_url(user_input, api_key)}')

if weather_data.json()['cod'] == '404':
    print('Город не найден')
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temp_C = round((temp - 32) * 5 / 9)

    print(api_view.view_weather(user_input, temp, temp_C, weather))
