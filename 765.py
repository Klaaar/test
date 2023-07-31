def summa_n():
    num = int(input("Введите положительное число: "))
    while num < 0:
        print("Положительное надо")
        num = int(input("Введите положительное число: "))
    p = 0
    i = 1
    while i <= num:
        p = p+i
        i += 1

    print("Я знаю, что сумма чисел от 1 до",num, "равна",p )
summa_n()