from tkinter import*
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.geometry("380x350+300+300")
window.title("Курс валют")
#---------------------------------------------
window.resizable(width=False, height=False)
#---------------------------------------------
canvas = Canvas(window,bg='#FFFACD',width=380, height=350)
canvas.pack()


url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req" : today}

responce = requests.get(url, params = payload)

xml = BeautifulSoup(responce.content, 'html.parser')

def getCourse (id):
    return xml.find('valute', {'id': id}).value.text

img_logo = PhotoImage(file='logo.png')
logo = Label(window, image=img_logo,bg='#FFFACD')
logo.place(x=0, y=0)

lab = Label(window, text='Курс валют\n MAXIMUM банк', fg='#BDB76B',bg='#FFFACD', font='Arial 22')
lab.place(x=150,y=25)

course_info = Label(window,text='Курс на: '+today.replace('/','.'),fg='#B8860B', font='Arial 18',bg='#FFFACD')
course_info.place(x=90,y=150)

usd_course = Label(window,text='Доллар: '+ getCourse('R01235'),fg='#B8860B', font='Arial 16',bg='#FFFACD')
usd_course.place(x=100,y=190)

e_course = Label(window,text='Евро: '+ getCourse('R01239'), fg='#B8860B',font='Arial 16',bg='#FFFACD')
e_course.place(x=100,y=215)

yuan_info = Label(window,text='Юани: '+ getCourse('R01375'),fg='#B8860B', font='Arial 16',bg='#FFFACD')
yuan_info.place(x=100,y=240)

window.mainloop()
