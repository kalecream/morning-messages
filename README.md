# Morning Messages

A simple python script to send cute messages to my boyfriend. See below for a sample output.

## Installation

 1. `git clone https://github.com/kalecream/morning-messages.git`
to get this repository

2. `pip3 install -r requirements.txt`
to install packages

3. Change the variables in the environment file.
```txt
NUMBER=+18881234567
CITY=
COUNTRY=
OPEN_WEATHER_API=
NAME=S
RSS_URL=
```

4. Run the script in /resources/cron.py when you are satisfied with your edits of the .env and morning_message.py

## Example Output

**This script works via Whatsapp Web and is designed to wait 15 seconds for the tab to load before pasting and sending the message.** You can reduce this time if you have faster internet or incease it for slower connections. PyWhatKit makes a txt file with your previous sent messages so you'll have a record of it.

```txt
✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧

I love how you bring the best of me whenever I am with you. Thank you for making my life a lot easier. Good morning, sunshine. Today is Tuesday, 16 November, 2021 and it's another day full of potential to give life some meaning. Night falls at 05:30 PM which gives you plenty of time to get things done!

♡ Weather Report ♡

The temperature today will be 31°C, but it feels like 33°C. The main thing for today 
in weather is Rain and they say there will be light rain. The sun is also pelting us 
at a UV index of 8.3 so extra protection needed.

♡ Latest News Report ♡

**‘Everyone knows I’m a snitch’**
A Jamaican man who was a state witness in a high-profile gang trial has got himself in trouble with the law in the territory to which he was dispatched under the Government’s witness protection programme but claims he is being shunned by local...

**Former conductor awarded millions for injuries after JUTC driver hits pothole**
THE SUPREME Court has ruled that the state-owned bus entity Jamaica Urban Transit Company (JUTC) should pay more than J$18 million to former conductor Joy Murray for injuries suffered on the job in 2002. Murray’s lawyer, Andrea Walter-Isaacs, told...

**Lawyer questions witness’ claim of don status**
The ex-crony of the One Don Gang testified on Monday that one of the 33 alleged members of the gang now on trial had told him that he had murdered a policeman in Portmore, St Catherine, but faced withering cross-examination questioning the...

Love Always,
Sab

ଘ(੭ˊ꒳​ˋ)੭✧
```

## Contributions

Contributions are welcomed! If you plan to contribute:

Create a new virtual environment
```py 
python -m venv venv
```

```activate virtual environment
source venv/bin/activate
```

Installing new packages
```py
python -m pip install <package-name>
```

Run before uploading if you've installed any extra dependencies!
```py 
pip3 freeze > requirements.txt
```

Deactivate the virtual environment
```py
deactivate
```
