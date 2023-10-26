"""Past Api_URL"""


def set_url(user_input, api_key, api_url='https://api.openweathermap.org/data/2.5/weather?q='):
    return api_url + user_input + '&units=imperial&APPID=' + api_key
