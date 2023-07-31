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
    button_url = telebot.types.KeyboardButton("Перейди, тут стишки", url="https://stihi.ru/")
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

#--------------------------------------------------------------------------------

@bot.message_handler(commands=["game_q"])
def send_game_q(message):
    games = "Какой жанр игр вас интересует?(MMORPG,RPG,пиксельные,шутеры)"
    bot.send_message(message.chat.id, games)
def game_MMORPG(message):
    MMORPG_g = "Могу посоветовать World of Warcraft,Guild Wars 2,RuneScape или Lost Ark"
    bot.send_message(message.chat.id, MMORPG_g)
def game_RPG(message):
    RPG_g = "Могу посоветовать Dark Souls 3,League of Legends,Cyberpunk 2077 или Deathloop"
    bot.send_message(message.chat.id, RPG_g)
def game_8_bit(message):
    g_8_bit = "Могу посоветовать Undertale,OMORI,Deltarune или TO THE MOON"
    bot.send_message(message.chat.id, g_8_bit)
def game_shooter(message):
    shooter_g = "Могу посоветовать Half-Life,Bleed 2,Hell is Other Demons или Unsighted"
    bot.send_message(message.chat.id, shooter_g)

@bot.message_handler(content_types=["text"])
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
        send_game_q(message)
    #------------------------------------------------------
    elif message.text.strip() == "MMORPG":
        game_MMORPG(message)
    elif message.text.strip() == "RPG":
        game_RPG(message)
    elif message.text.strip() == "пиксельные":
        game_8_bit(message)
    elif message.text.strip() == "шутеры":
        game_shooter(message)

bot.polling()