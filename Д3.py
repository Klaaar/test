from tkinter import *
import time
import random

window = Tk()
window.geometry('800x600')
canvas = Canvas(window, width=800, height=600, bg = 'white')
canvas.pack()


hp =100
dmg = 20

class un_1:
    def __init__(self):
        self.hp = hp
        self.dmg = dmg
        self.unit_1 = None
    def b_un_1(self):
        hp_1 = self.hp
        dmg_1 = self.dmg
        self.unit_1 = canvas.create_rectangle(160,100,200,200,fill='black',outline='')

class un_2:
    def __init__(self):
        self.hp = hp
        self.dmg = dmg
        self.unit_1 = None
    def b_un_1(self):
        hp_2 = self.hp
        dmg_2 = self.dmg
        self.unit_1 = canvas.create_rectangle(360,100,400,200,fill='green',outline='')




window.mainloop()