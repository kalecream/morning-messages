# Morning Messages

A simple python script to send cute messages to my boyfriend. It gives him the weather and news currently.

## Installation

1. `git clone https://github.com/kalecream/morning-messages.git`
to get this repository

2. `pip3 install -r requirements.txt`
to install packages

OR

2. Install `geopy.geocoders, Nominatim, Pywhatkit` and `Dotenv`

3. Change the variables in the environment file.

4. Follow the steps in this article to [add the file to Windows Scheduler](https://www.jcchouinard.com/python-automation-using-task-scheduler/)

```txt
NUMBER=+18881234567
CITY=KINGSTON
COUNTRY=JAMAICA
OPEN_WEATHER_API=73u589ghhkdty65
NAME=SABRINA
RSS_URL=https://jamaica-gleaner.com/feed/rss.xml
```
**This script works via Whatsapp Web and is designed to wait 15 seconds for the tab to load before pasting and sending the message.** You can reduce this time if you have faster internet or incease it for slower connections. PyWhatKit makes a txt file with your previous sent messages so you'll have a record of it.
## Example Output

```txt
✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧

I love how you bring the best of me whenever I am with you. Thank you for making my life a lot easier. Good morning, sunshine. Today is Tuesday, 16 November, 2021 and it's another day full of potential to give life some meaning. Night falls at 05:30 PM which gives you plenty of time to get things done!

♡ Weather Report ♡

The temperature today will be 31°C, but it feels like 33°C. The main thing for today 
in weather is Rain and they say there will be light rain. The sun is also pelting us 
at a UV index of 8.3 so extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of  SPF-15, broad-spectrum sunscreen on exposed skin.

♡ Latest News Report ♡

**‘Everyone knows I’m a snitch’**
A Jamaican man who was a state witness in a high-profile gang trial has got himself in trouble with the law in the territory to which he was dispatched under the Government’s witness protection programme but claims he is being shunned by local...

**Former conductor awarded millions for injuries after JUTC driver hits pothole**
THE SUPREME Court has ruled that the state-owned bus entity Jamaica Urban Transit Company (JUTC) should pay more than J$18 million to former conductor Joy Murray for injuries suffered on the job in 2002. Murray’s lawyer, Andrea Walter-Isaacs, told...

**Lawyer questions witness’ claim of don status**
The ex-crony of the One Don Gang testified on Monday that one of the 33 alleged members of the gang now on trial had told him that he had murdered a policeman in Portmore, St Catherine, but faced withering cross-examination questioning the...

Love Always,
Sabrina

ଘ(੭ˊ꒳​ˋ)੭✧
```

## Contributions

Contributions are welcomed! If you plan to contribute:

Please run `pip3 freeze > requirements.txt` before uploading if you've installed any extra dependencies!
