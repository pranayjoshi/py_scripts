from requests import get

def weather(city_name):
    if city_name == "":
        return "Enter the City name!"
    try:
        url2 = 'https://api.openweathermap.org/data/2.5/weather?appid=608e56270a3d78b4012bbfdda0f05234&q=' + city_name
        res = get(url2)
        database = res.json()

        temp = int(database['main']['temp'])
        wind = database['wind']['speed']
        overall = database['weather'][0]['main']
        temp -= 272.15
        temp = "{:.2f}".format(temp)
        final_val = (f'The Current weather in {city_name} is {overall}. The tempeture is {temp} degree. it\'s wind speed is {wind} km')
        return final_val
    except:
        return "Enter valid city name!"
if __name__ == "__main__":
    city = input()
    print(weather(city))

