from tkinter import *

window = Tk()
window.geometry('800x600')
#создаем холст 800x600 белого цвета
canvas = Canvas(window, width=800, height=600, bg = 'white')#создание холста
canvas.pack()#разместить холст

window.title('холсты всякие')
#создаем прямоугольник, первое-параматры 2-ух(верхний левый и правый нижний) углов пр-ка, второе заливка
#canvas.create_rectangle(10,10,110,110, fill='yellow', outline='')

#canvas.create_rectangle(10,10,220,220, fill='#40E0D0', outline='pink')
#canvas.create_rectangle(10,10,55,55, fill='#4B0082', outline='')

#canvas.create_polygon(10,260,60,200,110,260,fill='yellow', outline='')
#canvas.create_rectangle(20,260,100,360, fill='#4B0082', outline='')
#canvas.create_rectangle(30,290,90,330, fill='#40E0D0', outline='')

class House:
    def __init__(self, roof_color,wall_color,number):#__init__ сохраняет свойства класса(цвет крыши стен и тд)
        self.number = number
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.height = 130
        self.width = 140
        self.roof = None
        self.wall = None

    def build_house(self,x,y):
        h = self.height
        w = self.width

        self.roof = canvas.create_polygon(x,y,x+w,y,x+w/2,h-100,fill=self.roof_color, outline='')
        self.wall = canvas.create_rectangle(x+20,y,x+120,y+100, fill=self.wall_color, outline='')


# указываем атрибуты класса
house_1 = House('lavender', 'azure', 34)
#метод класа, рисуем дом
house_1.build_house(20,50)



window.mainloop()