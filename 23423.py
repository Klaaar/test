import telebot
import requests
import random
from bs4 import BeautifulSoup

token = "5784582397:AAEgKmZlZcdnHvfmLfIBn2gbexMqVYz2VdY"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message, res=False):
    welcome_text = 'привки'
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("факт")
    button2 = telebot.types.KeyboardButton("стих")
    button3 = telebot.types.KeyboardButton("котики")
    button4 = telebot.types.KeyboardButton("стикер")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = 'Муха села на варенье, вот и все стихотворенье...да..'
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton('Перейди, тут стишки', url='https://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id, 'Больше стишков по ссылке ниже', reply_markup=keyboard)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    fact_text = fact.text
    bot.send_message(message.chat.id, fact_link + fact_text)


@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1, 9))
    cat_img = open(cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGyAFjlcn6NwXCN0gfFcJfQ-iv-usiUAAC1CIAAvhtsEgTy0IAAWSuHYgrBA')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip() == 'факт':
        send_fact(message)
    elif message.text.strip() == 'стих':
        send_poem(message)
    elif message.text.strip() == 'котики':
        send_cat(message)
    elif message.text.strip() == 'стикер':
        send_sticker(message)

bot.polling()