import telebot
import requests
import random
from bs4 import BeautifulSoup#для работы с html разметкой

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    welcome_text = "приивеееет."
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=["poem"])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворение.."
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru")
    html = BeautifulSoup(response, "html parser")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))
    fact_link = fact.a.attrs["href"]
    bot.send_message(message.chat.id, fact_link)

bot.polling()