from tkinter import *
import random

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0

def p():
    global points
    points += 1

b = Button(
text='Нажми меня',
font=('TimesNewRoman', 24),
fg='white',
command=p
)
b.place(x=200, y=130)

if points == 20:
    b.update(fg= "#00FF00")
window.mainloop()

