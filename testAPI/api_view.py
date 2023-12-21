"""View Weather"""


def view_weather(user_input, temp, temp_C, weather):
    # print(weather_data.status_code)
    # print(weather_data.json())
    print(f'Температура в {user_input}: {temp} F, {temp_C} C')
    print(f'Погодные условия: {weather}')
