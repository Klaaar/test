#type - говорит какой тип данных в перемнной
#----------------------------------------------
#a = "Поздравляю со стартом второго модуля!"
#print(a[])
#----------------------------------------------
#for i in range(20,9,-2):
#    print(i)
#----------------------------------------------
#вывод с помощью f-строк
#n_1 = int(input())
#n_2 = int(input())
#print(f"сумма {n_1} и {n_2} чисел равна")#если что-то в {}-скобках - мы выходим из строки
#---------------------------------------------
def calc():
    print("Укажите интересующую вас операцию")
    print("* - умножение")
    print("- - вычитание")
    print("+ - сложение")
    print("/ - деление")
    oper = input()

    if oper == "*":
        num1 = input()
        num2 = input()
        try:
           res = int(num1) * int(num2)
        except ValueError: #ValuError - часть Except
            print("Ошибка")
        else:
            print(res)
    elif oper == "/":
        num1 = input()
        num2 = input()
        try:
            res = int(num1) / int(num2)
        except ValueError:
            print("Ошибка")
        else:
           print(res)
    elif oper == "-":
        num1 = input()
        num2 = input()
        try:
            res = int(num1) - int(num2)
        except ValueError:
            print("Ошибка")
        else:
           print(res)
    elif oper == "+":
        num1 = input()
        num2 = input()
        try:
            res = int(num1) + int(num2)
        except ValueError:
            print("Ошибка")
        else:
            print(res)
    elif oper == "^":
        num1 = input()
        num2 = input()
        num3 = input()
        try:
           res = int(num2) * int(num2) - 4* int(num1)* int(num3)
        except ValueError:
            print("Ошибка")
        else:
           print(res)
    else:
        print("Операция неизвестна, повторите ввод")
    print("")
    calc()
calc()
#----------------------------------------------------------
