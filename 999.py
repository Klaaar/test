

import telebot
import requests
import random
from bs4 import BeautifulSoup

#----------- декораторы------------
#функция-обертка
#def my_decorator(func_to_decorate):
#    def decorated_func():
#        print("Я начинаю работать")
#        #функция для которой нужна обертка
#        func_to_decorate
#        #код который выполнится после работы функции
#        print("Я закончил работу")
#        #возвращаем функцию-обертку
#    return decorated_func

#@my_decorator
#def my_func():
#    print("Я работаю")
#
#my_func()
#------------че то не так идет------------

token = "5784582397:AAEgKmZlZcdnHvfmLfIBn2gbexMqVYz2VdY"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    welcome_text = "Здравствуй! Я умею рассказывать стишки, знаю интересные факты и у меня есть.. фотографии котиков;D"
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=["poem"])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворение.. *смех за кадром*"
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru").content #подключение к сайту и вытягивание к html разметке
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))#рандомный факт по тегу
    fact_link = fact.a.attrs["href"] #из словаря значение(гипперсылка, то что отправляем)
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=["cat"])
def send_cat(message):
    cat_number = str(random.randint(1,9))
    cat_img = open(cat_number+".jpg", "rb")
    bot.send_message(message.chat.id, cat_img)

bot.polling()