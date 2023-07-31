var = True
var2 = False
print(type(var))

time = int(input('Сколько сейчас времени?Введите число от 0 до 23 '))

if time >= 8 and time < 12:
    print('Доброе утро')
elif time >= 12 and time < 16:
    print('Добрый день')
elif time >= 16 and time <= 21:
    print('Добрый вечер')
elif (time >= 22 and time <= 24) or (time >= 0 and time < 8) :
    print('Доброй ночи')