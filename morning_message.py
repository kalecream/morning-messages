import pywhatkit, random
NUMBER = "+18881234567"


content = [
    "Good morning, sweetheart. Wishing you a wonderful day filled with joy, fun, and every ounce of happiness. I love you so much.",
    "Good morning baby. I just wanted you to know how much I care for you. Have an amazing day.",
    "Have a great day my love. Thank you for making every day special and memorable for me. I love you so much.",
    "I love how you bring the best of me whenever I am with you. Thank you for making my life a lot easier, love. Good morning, sunshine."]

header = [
    "⋆༶❀.⋆｡⋆༶˙⊹ .⋆. ｡⋆༶⋆˙⊹❀⋆｡⋆༶⋆˙⊹",
    "-ˋˏ ༻❁༺ ˎˊ-",
    "♡",
    "🍓☽。･:*:･",
    "♡︶꒦꒷♡꒷꒦︶♡",
    " ⋆୨୧ ₊ﾟ🥡🥢 ⊹ɞ ",
    "🦋☆*: .｡. ♡ .｡.:*☆🦋",
    "(っ◔◡◔)っ💝",
    "(✿◠‿◠)ッ 🐻🌻",
    "˖˵˵˵˵˵˵ଘ( ꈍᴗꈍ)⋆🌷"]

kaomoji = [
    "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
    "°˖✧◝(⁰▿⁰)◜✧˖°",
    "(づ￣ ³￣)づ",
    "(｡•̀ᴗ-)✧",
    "ʕ •ᴥ• ʔ",
    "ʕ ᵔᴥᵔ ʔ",
    "ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊˚",
    "ଘ(੭ˊ꒳​ˋ)੭✧",
    "(ෆ˙ᵕ˙ෆ)♡",
    "(づᴗ _ᴗ)づ♡"]

msg = random.choice(header) + "\n\n" + random.choice(content) + "\n\n" + random.choice(kaomoji) + "\n\n"
print(msg)

#pywhatkit.sendwhatmsg_instantly(NUMBER,msg,20,False)