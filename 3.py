#f = open("tex4t.txt")
#print(f.read()) #считывает как есть??
#print(f.readline()) #построчная обработка
#print(f.readlines()) #выводит все строки списком, указывая переход на новую строку \n

#for line in f:
   # print(int(line))

#f = open("tex4t.txt", "w") #w-режим перезаписи удаляет всё
#f.write("\n346345")#добавляем строковый тип данных
#f.close() #добавить после изменений

#f = open("tex4t.txt", "a") #a-режим добавления с сохранением преж инфы
#f.write("\n346345")#добавляем строковый тип данных
#f.close() #добавить после изменений

#def summa(x,y):
  #  return x + y
#def g(x,y):
   # return x - y

#a = int(input())
#f = int(input())
#k = input("Введите опер + или -")

#if k == "+":
   # print(summa(a, f))
#elif k == "-":
 #   print(g(a, f))




@bot.message_handler(commands=["secret"])
def send_lol(message):
    lol_text = "Хэй..никто не знает, но у меня есть инфа о новом проекте создателя Sally Face!1!, тебе очень повезло, что специально для тебя я раскрою эту информацию..  https://youtu.be/PdWPszqMYrY "
    bot.send_message(message.chat.id, lol_text)



