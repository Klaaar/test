from tkinter import*
import tkinter
import time

window = Tk()
window.geometry("350x200")
window.resizable(width=False,height=False)
window.config(bg="black")
window.title("Кликер")

b=tkinter.Button(text="Example")
for i in range(50):
    i+=1
    b.place(x=i, y=i)
    time.sleep(0.1)
window.mainloop()