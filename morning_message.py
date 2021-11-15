import pywhatkit, random
from dotenv import dotenv_values
import resources.kaomoji as kaomoji, resources.messages as messages

secret = dotenv_values(".env")

msg = random.choice(kaomoji.header) + "\n\n" + random.choice(messages.content) + "\n\n" + random.choice(kaomoji.happy_kaomoji) + "\n\n"
print(msg)

pywhatkit.sendwhatmsg_instantly(secret["NUMBER"],msg,20,False)