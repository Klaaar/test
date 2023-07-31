import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
while True:
    with sr.Microphone(device_index=1) as source:
        print('скажи что-нибудь...')
        audio = r.listen(source)
    speech = r.recognize_google(audio, language='ru_RU', show_all = True)
    a = speech['alternative']
    print('Вы сказали: ', a['transcript'])

   
