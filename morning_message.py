import pywhatkit, random, requests
from geopy.geocoders import Nominatim
from dotenv import dotenv_values, main
from datetime import datetime
import resources.kaomoji as kaomoji, resources.messages as messages

secret = dotenv_values(".env")

geolocator = Nominatim(user_agent="morning_message")
location = geolocator.geocode(secret["CITY_NAME"] + "," + secret["COUNTRY_NAME"])

try:
    weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&exclude=minutely,hourly,daily&units=metric&appid="+secret["OPEN_WEATHER_API"])
    weather.raise_for_status()
    weather_data = weather.json()
    sunset =  datetime.utcfromtimestamp(weather_data["current"]["sunset"]+weather_data["timezone_offset"]).strftime("%I:%M:%S %p")
    today = datetime.utcfromtimestamp(weather_data["current"]["sunset"]+weather_data["timezone_offset"]).strftime("%A, %B %m, %Y ")
    temperature = weather_data["current"]["temp"]
    feels_like = weather_data["current"]["feels_like"]
    main_weather = weather_data["current"]["weather"][0]["main"]
    weather_report = weather_data["current"]["weather"][0]["description"]
except weather.exceptions.HTTPError as error:
    print(error)
    print("Weather data not found. \nDid you add an API Key to .env?")
    today, sunset, temperature, feels_like, main_weather, weather_report =  None

if today is None:
    msg = random.choice(kaomoji.header) + "\n\n" + random.choice(messages.content) + "\n\n" + random.choice(kaomoji.happy_kaomoji) + "\n\n"
else:
    msg = random.choice(kaomoji.header) + "\n\n" + random.choice(messages.content) + " Today is " + today + "and it's another day full of potential to give life some meaning. Night falls at " + sunset + " which gives you plenty of time!"+ "\n\n" + "♡ Weather Report ♡\n\n" + "The temperature today is " + str(temperature) + "°C, but it wil feel like " + str(feels_like) + "°C. The main thing for today in weather is " +  main_weather + " and they say there will be " + weather_report + ".\n\n" + "Love Always,\n"+ secret["NAME"] +  "\n\n" + random.choice(kaomoji.happy_kaomoji or kaomoji.kiss_kaomoji or kaomoji.love_kaomoji)
print(msg)

pywhatkit.sendwhatmsg_instantly(secret["NUMBER"],msg,20,False)