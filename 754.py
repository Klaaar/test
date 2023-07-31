from tkinter import*
import time

window = Tk()
window.geometry("350x200")
window.resizable(width=False,height=False)
window.config(bg="black")
window.title("Кликер")

points = 0
points_2 = 0
f = 0
f_2 = 0
def b_1():
    global points, f_2
    global f
    points += 1
    if points == 10:
        button_2["text"] = "Ну пожалуйста"
        time.sleep(1)

def b_2():
    global points_2, f
    global f_2
    points_2 += 1
    if points_2 == 10:
        button["text"] = "Ну пожалуйста"
        time.sleep(1)

button = Button(text="чтобы кликать", bg= "#000000", fg= "#FFFFFF", command=b_1)
button.place(x=50, y=80)

button_2 = Button(text="тоже чтобы кликать", bg= "#000000", fg= "#FFFFFF", command=b_2)
button_2.place(x=180, y=80)

window.mainloop()