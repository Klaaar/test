import os
from pygame import mixer
from gtts import gTTS

my_file = open('golos_helper.txt', 'r')
my_string = my_file.read()


mixer.init()#активируем функции??

tts = gTTS(text=my_string, lang='ru')#кого и как читать
tts.save('golos_helper.mp3')
mixer.music.load('golos_helper.mp3')#соранить как мп3
mixer.music.play()

