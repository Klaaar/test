from tkinter import*
import time

window = Tk()#создаёт окно в переменной
window.geometry("900x300")
window.resizable(width=False,height=False)
window.config(bg="black")
text = Label(text="Ваш компутер заражён!1!", fg="#000000", bg="#2E8B57", font=("Courier New", 35))
text.place(x=100, y=100, width=700, height=100)
count_text = Label(text="6", fg="#000000", bg="#2E8B57", font=("Courier New", 39))

def on_close():
   if int(count_text["text"]) > 0:
       count_text["text"] = int(count_text["text"])-1
       count_text.place(x=250,y=25, width=400, height=100)
       window.after(1000, on_close())#функция для окна которая позволяет что-то делать спутя какое-то время(функцию и тп)
   else:
       count_text["text"] = 0
       width = window.winfo_screenwidth()    #|замеряет экран
       height = window.winfo_screenheight()  #|
       window.geometry(str(width)) + "x" + str(height)#пиринмает текст!!!
       photo = PhotoImage(file="D:\с рабочего стола")
       label = Label(image=width, height=height, x=0, y=0)
       label.image = photo
       label.place(width=width, height=height, x=0, y=0)






window.protocol("WM_DELETE_WINDOW", on_close)#описывает действия виджета(принимает кнопку и функцию, которая "включается" при нажатии на эту кнопку)






window.mainloop()













