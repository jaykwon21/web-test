import os
from gtts import gTTS
from playsound import playsound
# library
# python library
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print("hello, World!")
text = "[1] hello : This is test"
tts = gTTS(text=text, lang='en')

tts.save("hi2.mp3")
playsound("hi2.mp3")

  