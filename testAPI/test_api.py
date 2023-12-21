"""Weather API"""
import requests

api_key = 'adfcc0c9fb5b2a15a8ce28375f9069a4'

user_input = input('Введите город: ')

weather_data = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}')

if weather_data.json()['cod'] == '404':
    print('Город не найден')
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temp_C = round((temp - 32) * 5 / 9)

    # print(weather_data.status_code)
    # print(weather_data.json())
    print(f'Температура в {user_input}: {temp} F, {temp_C} C')
    print(f'Погодные условия: {weather}')
