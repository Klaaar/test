from fpdf import FPDF

pdf = FPDF("P", "cm", (10,15))
pdf.add_page()

pdf.add_font("courier", "", "C:\WINDOWS\FONTS\COUR.ttf", uni=True)

pdf.set_font("courier", size=16)
pdf.set_text_color(50, 205, 50)#цвет текста
pdf.set_fill_color(0, 128, 0)#заливка вокруг текста
pdf.set_draw_color(0, 0, 0)

pdf.cell(10,5, txt="Пумпумпурум", align="C", border=1, fill=True)

pdf.image("fon.jpg", h=0, w=10, x=0, y=5)

pdf.output("testpdf.pdf")










