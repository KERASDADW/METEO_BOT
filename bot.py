import requests
city = "Moscow,RU"
appid = "8a7acef785757a4ab030d37df7109cd7"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print (data)
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра (м/с):",data['wind']['speed'])
print("Видимость (м):",data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
int(i['main']['temp']), "> \r\nПогодные условия <",
i['weather'][0]['description'], ">\r\nСкорость ветра <",i['wind']['speed'],"м/с> \r\nВидимость<",i['visibility'],"м>\n")
print("____________________________")