#text to speech
from gtts import gTTs 
import os
my_text="Raveendra is good boy and hs is comeing from kadapa distic and he studying at tirupati"
language="te"
output=gTTs(tex=my_text,lang=language,slow=True)
output.save("output.mp3")
os.system("start output.mp3")

