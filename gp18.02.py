#import os
#from pygame import mixer
#from gtts import gTTS

#my_file = open('golos_helper.txt', 'r')
#my_string = my_file.read()
#my_file.close()

#mixer.init()

#tts = gTTS(text=my_string, lang='en')
#tts.save('golos_helper.mp3')
#mixer.music.load('golos_helper.mp3')
#mixer.music.play()

import pyaudio
import speech_recognition as sr
import random

r = sr.Recognizer()
films = ['Чебурашка', 'Аватар', 'Люди в черном']
def film_ch():
    while True:
        with sr.Microphone(device_index=1) as source:
            print('скажи что-то')
            audio = r.listen(source)
        speech = r.recognize_google(audio, language='ru_RU', show_all=True)
        alt = speech['alternative'][0]
        alt_list = alt['transcript']
        if alt_list == 'фильм':
            film = random.randint(0, len(films) - 1)
            print(films[film])
        else:
            print('повторите')
film_ch()


