import telebot
import requests
import random
from bs4 import BeautifulSoup

token = "5784582397:AAEgKmZlZcdnHvfmLfIBn2gbexMqVYz2VdY"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message, res=False):
    welcome_text = "Здравствуй!"
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("факт")
    button2 = telebot.types.KeyboardButton("котики")
    button3 = telebot.types.KeyboardButton("стих")
    button4 = telebot.types.KeyboardButton("стикер")

    button5 = telebot.types.KeyboardButton("совет по игре")

    keyboard.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, welcome_text, reply_markup= keyboard)

@bot.message_handler(commands=["poem"])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворение..    *смех за кадром*"
    bot.send_message(message.chat.id,poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)#row_width - кол-во столбцов
    button_url = telebot.types.KeyboardButton("Перейди, тут стишки", url = "https://stihi.ru/")
    keyboard.add(button_url)
    bot.send_message(message.chat.id, "стишки",reply_markup= keyboard)

@bot.message_handler(commands=["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru").content #подключение к сайту и вытягивание к html разметке
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))#рандомный факт по тегу
    fact_link = fact.a.attrs["href"] #из словаря значение(гипперсылка, то что отправляем)
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=["stiker"])
def send_st(message):
    bot.send_message(message.chat.id, "CAACAgIAAxkBAAEGyAFjlcn6NwXCN0gfFcJfQ-iv-usiUAAC1CIAAvhtsEgTy0IAAWSuHYgrBA")

@bot.message_handler(commands=["cat"])
def send_cat(message):
    cat_number = str(random.randint(1,9))
    cat_img = open(cat_number+ ".jpg", "rb")
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=["secret"])
def send_lol(message):
    lol_text = "Хэй..никто не знает, но у меня есть инфа о новом проекте создателя Sally Face!1!, тебе очень повезло, что специально для тебя я раскрою эту информацию..  https://youtu.be/PdWPszqMYrY "
    bot.send_message(message.chat.id, lol_text)

@bot.message_handler(commands=["game"])
def send_game(message):
    game_q = "Какой жанр игр Вас интересует?"
    bot.send_message(message.chat.id, game_q)







@bot.message_handler(commands=["text"])
def answer(message):
    if message.text.strip() == "факт":
        send_fact(message)
    elif message.text.strip() == "котики":
        send_cat(message)
    elif message.text.strip() == "стикер":
        send_st(message)
    elif message.text.strip() == "стих":
        send_poem(message)
    elif message.text.strip() == "совет по игре":
        send_game(message)


bot.polling()