# class Item:
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __add__(self, other):
#         if isinstance(other,Item):
#             return self.price + other.price
#         elif isinstance(other,int):
#             return self.price + other
#
# item1 = Item('Видеокарта', 15000, 0.8)
# item2 = Item('Процессор', 12000, 0.3)
#
# total_price = item1.price + item2.price
# print(total_price)
# total_price2 = item1.price + 1000
# print(total_price2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import*
import random

window = Tk()
window.geometry('600x600')

class Clay:
    image = PhotoImage(file='clay.png').subsample(4,4)#чтобы одинаковые были

class Fire:
    image = PhotoImage(file='fire.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other,Earth):#isinstance проверяет принадлежность к классу
            return Clay
class Water:
    image = PhotoImage(file='water.png').subsample(4,4)
class Wind:
    image = PhotoImage(file='wind.png').subsample(4,4)
class Earth:
    image = PhotoImage(file='earth.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other,Fire):
            return Clay
canvas = Canvas(window,width=600)
canvas.pack()

elements = [Fire(),Earth(),Water(),Wind()]
for elem in elements:
    ing = canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)

window.bind('<B1-Motion>')
window.mainloop()