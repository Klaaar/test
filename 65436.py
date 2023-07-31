number = int(input("Введите число: "))
summ = number
while number != 0:

    summ += number
    number = int(input("Введите число: "))

print(summ)