#dict = {"яблоко": "apple",
        #"молоко": "milk",
       # "кот": "cat",
        #"собака": "dog",
       # "привет":"hello"}

#print(*dict)#выводит ТОЛЬКО все КЛЮЧИ словаря

#обращение по ключу(выводит ЗНАЧЕНИЕ), если обратиться к ключу, который повторяется, то выводит последнее ЗНАЧЕНИЕ
#print(dict["привет"])

#добавление элемента

#dict["развитие"] = "development"
#print(dict)

#добавление элементОВ

#dict.update({"дом": "home", "небо":"sky"})
#print(dict)

#замена элемента(ЗНАЧЕНИЯ)

#dict["привет"] = "hi"
#dict.update({"дом":"small", "яблоко":"green"})
#print(dict)

#удаление элемента(в скобках нужен КЛЮЧ)

#del dict["молоко"]
#print(dict)

#удаление элемента + его сохранение( обращаемся по ключу, но сохраненный-удаленный элемент выводится как значение)
#pop - сохраняет, но удаляет из словаря

#delword = dict.pop("молоко")
#print(dict)
#print(delword)

#------------------------------

questions = [

        {"question":"Кто будет являться символом 2023 года?",
        "answers": ["Тигр", "Кролик", "Змея", "Бык"],
        "right_answer": 1 },

        { "question":"Какое новогоднее блюдо соответствует цвету Pantone 2023?",
        "answers": ["Оливье", "Сельд под шубой", "Крабовый салат", "Утка"],
        "right_answer": 1 },

        {"question":"Как называют Деда Мороза в Швеции?",
        "answers": ["Санта Клаус", "Дед Мороз", "Тонте", "Бобои Барфи"],
        "right_answer": 2 }
]

for quest in questions:
        print(quest.get("question"))#get - один из способов обращения к КЛЮЧУ СЛОВАРЯ
        number = 0
        for answ in quest["answers"]:
                number += 1
                print(number, answ)
        user_number = int(input("Ваш ответ: "))
        if user_number - 1 == quest.get("right_answer"):#вычитаем из ответа ЮзЕрА 1 т к его ответ на 1 больше чем индекс ответа
                print("Верно :D")
        else:
                print("не верно.")
        print("-"*20)














