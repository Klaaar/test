from tkinter import *
import random
#шаблон окна
window = Tk()
w = 600#то же, что и geomtry, полезно при присутсвии input()
h = 600
window.geometry(str(w)+'x'+str(h))
#создаем холст для игрого поля
canvas = Canvas(window,width=w,height=h)
canvas.place(in_ = window,x=0,y=0)#то же, что и pack(), но тут уже нужно указывть, ГДЕ размещать
#фон игры
bg_p = PhotoImage(file='bg_2.png')
#Класс рыцаря
class Knight:
    def __init__(self):
    #координаты центра рыцаря
        self.x = 70
        self.y = h//2
    #cкорость рыцаря
        self.v = 0
    #изображение рыцаря
        self.photo = PhotoImage(file='knight.png')
    #функция движения вверх и вниз и остановки
    def up(self, event):
        self.v = -3
    def down(self, event):
        self.v = 3
    def stop(self, event):
        self.v = 0
#класс для дракона
class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100,500)
        self.v = random.randint(1,3)
        self.photo = PhotoImage(file='dragon.png')
knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    global dragon
    canvas.delete('all')
    canvas.create_image(300,300, image =bg_p )
    canvas.create_image(knight.x,knight.y, image=knight.photo)
    knight.y += knight.v

    current_dragon = 0
    dragon_to_kill = -1


    for dragon in dragons:
        dragon.x-=dragon.v
        canvas.create_image(dragon.x,dragon.y,image=dragon.photo)

        if ((dragon.x-knight.x)**2 + (dragon.y-knight.y)**2)**2<=96**2:
            dragon_to_kill = current_dragon

        current_dragon += 1

        if dragon.x <=0:
            canvas.delete('all')
            canvas.create_text(w//2,h//2,text='Вы проиграли.', font='Veranda 42', fill='red')
            break
    if dragon_to_kill >=0:
        del dragons[dragon_to_kill]
    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w//2,h//2,text='Вы проиграли.', font='Veranda 42', fill='red')
    else:
        window.after(5, game)
game()
window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.mainloop()