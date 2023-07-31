from fpdf import FPDF
from datetime import datetime

pdf = FPDF("P", "mm", "A4")# pdf *конкретно здесь* это кста просто переменная
pdf.add_page()

pdf.image("fon.jpg", h=297,w=210, x=0,y=0)# x=0,y=0 - левый верхний угол

pdf.add_font("comic", "", "C:\WINDOWS\FONTS\COMIC.ttf", uni=True)#C:\WINDOWS\FONTS\COMIC.ttf - путь для всех шрифтов(установленных)
pdf.set_font("comic", size=40)#    }  прям шаблон текста типо
pdf.set_text_color(34, 139, 34)#   }

friend_name = input("Введите имя человека, которого хотите поздравить ")

pdf.cell(0, 95, ln=1)
pdf.cell(0, 20, txt="Дорогая " + friend_name + "!", align="C", ln=1)

pdf.set_font("comic", size=20)
pdf.set_text_color(34, 139, 34)
pdf.set_right_margin(50)
pdf.set_left_margin(50)
pdf.multi_cell(0, 20, txt=input("Введите поздравление ") + "!", align="C")

today = datetime.today().strftime("%d.%m.%Y")#день, месяц, год
pdf.set_text_color(34, 139, 34)
pdf.cell(0,10, txt=today, align="R", ln=1)#ln это.. кол-во строк в одностроч функции..

pdf.cell(0, 10, txt=input("Подпишись ") , align="R", ln=1)

pdf.output("card.pdf")