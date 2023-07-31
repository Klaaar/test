from tkinter import*

window = Tk()
window.geometry("700x500")#размер окна, мнежу ними англ х
window.title("Викторина: Интересные факты")#наиминование окна

facts = [
    {"text":"При рождении у человека в 2 раза больше нейронов", "right":1},
    {"text":"Нил - самая длинная река", "right":1},
    {"text":"Земля плоская", "right":0}
    ]

index_dict = 0
points = 0
var=IntVar
def check():
    global index_dict, points
    answer = var.get()
    if bool(answer) == facts[index_dict]["right"]:
        points += 1
    if index_dict < len(facts)-1:
        index_dict += 1
        facts["text"] = facts[index_dict]["text"]]
    else:
        points_label = Label(text="Вы набрали"+str(points),  font =("Comic Sans MS", 25), fg= "#000000", bg="#2E8B57")
        points_label.place(x=0,y=0,width=700, height = 50)



#однострочный виджет
label_title = Label(text = "Викторина: Правда или Ложь", font =("Comic Sans MS", 25), fg= "#000000", bg="#2E8B57")

label_title.place(width=700, height=50,x=0,y=0)
#многостроч виджет
fact = Message(text = facts[index_dict]["text"], font =("Comic Sans MS", 17), fg= "#000000", width=680,borderwidth=0)
fact.configure(justify=CENTER)
fact.place(x=30, y=80)


true = Radiobutton(text = "Правда", font = ("Comic Sans MS", 15), fg= "#000000", variable=var, value=1)
true.place(x=30, y=130)

false = Radiobutton(text = "Ложь", font = ("Comic Sans MS", 15), fg= "#000000",  variable=var, value=0)
false.place(x=30, y=170)

b =Button(text="Ответить", font = ("Comic Sans MS", 15), fg= "#000000", bg="#2E8B57", command = check )
b.place(x=200, y=150)


#не работает..

window.mainloop()#открыть окно, эта строчка всегда последняя





