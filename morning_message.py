import pywhatkit, random
from dotenv import load_dotenv
import resources.kaomoji as kaomoji, resources.messages as messages

load_dotenv(NUMBER)

msg = random.choice(kaomoji.header) + "\n\n" + random.choice(messages.content) + "\n\n" + random.choice(kaomoji.happy_kaomoji) + "\n\n"
print(msg)

pywhatkit.sendwhatmsg_instantly(NUMBER,msg,20,False)