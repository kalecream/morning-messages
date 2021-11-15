# Morning Messages

A simple python script to send cute messages to my boyfriend. It gives him the weather, news 

## Installation

1. `git clone https://github.com/kalecream/morning-messages.git`
to get this repository

2. `pip3 install -r requirements.txt`
to install packages (I need to clean up this file currently. It has some extra packages)

OR

Install geopy.geocoders, Nominatim, pywhatkit and dotenv

3. Change the phone number, city and country in the environment file.

```txt
NUMBER=+18881234567
CITY=KINGSTON
COUNTRY=JAMAICA
OPEN_WEATHER_API=73u589ghhkdty65
NAME=SABRINA
RSS_URL=https://jamaica-gleaner.com/feed/rss.xml
```

## Example Output

```txt
⋆༶❀.⋆｡⋆༶˙⊹ .⋆. ｡⋆༶⋆˙⊹❀⋆｡⋆༶⋆˙⊹

Couldn’t wait to text you good morning! Have a lovely day, babe. Today is Monday, November 11, 2021 and it's another day full of potential to give life some meaning. Night falls at 05:30 PM which gives you plenty of time!

♡ Weather Report ♡

The temperature today will be 31°C, but it feels like 36°C. The main thing for today in weather is Rain and they say there will be light rain. The sun is also pelting us. At a UV index of 7.4: Number below zero or missing data.

♡ Latest News Report ♡

EMERGENCY!
While staunchly defending the reimposition of states of emergency (SOEs) on Sunday, a combative Prime Minister Andrew Holness argued that his administration would not stand by and do nothing in the face of a tidal wave of deadly crime. In...

Betrayal, bloodshed traumatise victims years later
COMFORT, Manchester: Her reconstructed arm with 13 pins and a hand with three missing fingers are the macabre reminders of the hellish ordeal 69-year-old Deslyn Gordon survived 10 years ago in Comfort at the hands of man who tried to kill her and...

Pre-emptive strike
Amid a pending ruling on the constitutionality of specific detentions under states of emergency (SOE), the Government insisted Sunday that it has the power to hold persons without preferring charges as a pre-emptive mechanism to prevent crime. The...

Love Always,
Sabrina

ଘ(੭ˊ꒳​ˋ)੭✧
```

## Contributions

Contributions are welcomed! If you plan to contribute:

`pip3 install virtualenv`
to install a virtual environment.

`vitualenv messages`
to enter the virtual environment

`pip3 install -r requirements.txt`
to install all packages

---

Please run `pip3 freeze > requirements.txt` before uploading if you've installed any extra dependencies!
