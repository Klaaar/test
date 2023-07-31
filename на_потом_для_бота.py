@bot.message_handler(commands=["secret"])
def send_lol(message):
    h = "жми"
    p = "https://youtu.be/dQw4w9WgXcQ"
    h=p
    lol_text = "Хэй..никто не знает, но у меня есть инфа о новом проекте создателя Sally Face!1!, тебе очень повезло, что специально для тебя я раскрою эту информацию..   "
    bot.send_message(message.chat.id, lol_text)