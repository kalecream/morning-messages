import pywhatkit, random, requests
from geopy.geocoders import Nominatim
from dotenv import dotenv_values, main
from datetime import datetime
import resources.kaomoji as kaomoji, resources.messages as messages, resources.parse_rss as rss

secret = dotenv_values(".env")


geolocator = Nominatim(user_agent="morning_message")
location = geolocator.geocode(secret["CITY_NAME"] + "," + secret["COUNTRY_NAME"])

try:
    weather_api = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&exclude=minutely,hourly&units=metric&appid="+secret["OPEN_WEATHER_API"])
    weather_api.raise_for_status()
except weather_api.exceptions.HTTPError as error:
    print(error)
    today  =  None

weather_data = weather_api.json()
sunset =  datetime.utcfromtimestamp(weather_data["daily"][datetime.today().weekday()]["sunset"]+weather_data["timezone_offset"]).strftime("%I:%M %p")
today = datetime.today().strftime("%A, %B %m, %Y ")
temperature = weather_data["daily"][datetime.today().weekday()]["temp"]["day"]
feels_like = weather_data["daily"][datetime.today().weekday()]["feels_like"]["day"]
main_weather = weather_data["daily"][datetime.today().weekday()]["weather"][0]["main"]
weather_report = weather_data["daily"][datetime.today().weekday()]["weather"][0]["description"]
uv_index = weather_data["daily"][datetime.today().weekday()]["uvi"]
if uv_index >= 8:
    uv_info = "Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of  SPF-15, broad-spectrum sunscreen on exposed skin."
elif uv_index <= 7 and uv_index >= 3:
    uv_info = "Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses."
elif uv_index <=2 and uv_index >= 0:
    uv_info = "No protection needed. You can safely stay outside using minimal sun protection."
else:
    uv_info = "Number below zero or missing data."

news_df = rss.get_feed(secret["RSS_URL"])
news_df = news_df.drop(columns=['pubDate', 'guid']).iloc[:3]

if today is None:
    weather = "\n\n" + "♡ Weather Report ♡\n\n" + "Not retrieved. \n\n"
else:
    weather = "\n\n" + "♡ Weather Report ♡\n\n" + "The temperature today will be " + str(round(temperature)) + "°C, but it feels like " + str(round(feels_like)) + "°C. The main thing for today in weather is " +  main_weather + " and they say there will be " + weather_report + ".\n The sun is also pelting us. At a UV index of " + str(uv_index) + ": " + uv_info + "\n\n"

greeting = random.choice(kaomoji.header) + "\n\n" + random.choice(messages.content) + " Today is " + today + "and it's another day full of potential to give life some meaning. Night falls at " + sunset + " which gives you plenty of time!"

ending =  "\n\nLove Always,\n"+ secret["NAME"] +  "\n\n" + random.choice(kaomoji.happy_kaomoji or kaomoji.kiss_kaomoji or kaomoji.love_kaomoji)



story = "\n\n" + "♡ Latest News Report ♡\n\n" + news_df.iloc[0]['title'] + "\n" + news_df.iloc[0]['description'] + "\n\n" + news_df.iloc[1]['title'] + "\n"+ news_df.iloc[1]['description'] + "\n\n" + news_df.iloc[2]['title'] + "\n"+ news_df.iloc[2]['description']

msg = greeting + weather + story + ending

pywhatkit.sendwhatmsg_instantly(secret["NUMBER"],msg,15,False)
#pywhatkit.sendwhats_image(secret["NUMBER"], "/resources/img/cat1.png", msg)