import math
import time


while True:
    l = ['1. Сложить 2 числа', '2. Вычесть второе из первого', '3. Перемножить два числа',
         '4. Разделить первое на второе', '5. Возвести в степень N первое число', '6. Найти квадратный корень из числа',
         '7. Найти факториал', '8. Найти синус', '9. Найти косинус', '10. Найти тангенс', '11. ВЫХОД']
    for j in l:
        print(j)
    m = input("Введите действие ")
    try:
        m = int(m)
    except:
        print("Вы ввели некоректное действие")
        continue
    if m > 12 or m < 1:
        print("Вы ввели некоректное действие")
    if m == 1 or m == 2 or m == 3 or m == 4:
        try:
            n1 = float(input("Введите первое число "))
            n2 = float(input("Введите второе число "))
        except:
            print("Вы ввели некорректные данные")
            continue
        if m == 1:
            print(n1 + n2)
        elif m == 2:
            print(n1 - n2)
        elif m == 3:
            print(n1 * n2)
        elif m == 4:
            if n2 == 0:
                print("На ноль делить нельзя")
            else:
                print(n1/n2)
    elif m == 5:
        try:
            n1 = float(input("Введите число "))
            n2 = float(input("Введите степень "))
        except:
            print("Вы ввели некорректные данные")
            continue
        print(math.pow(n1, n2))
    elif m == 6 or m == 8 or m == 9:
        try:
            n1 = float(input("Введите число "))
        except:
            print("Вы ввели некорректные данные")
            continue
        if m == 6:
            print(math.sqrt(n1))
        elif m == 8:
            print(math.sin(math.radians(n1)))
        elif m == 9:
            print(math.cos(math.radians(n1)))
        elif m == 10:
            print(math.tan(math.radians(n1)))
    elif m == 7:
        try:
            n1 = int(input("Введите число "))
        except:
            print("Вы ввели некорректные данные")
            continue
        print(math.factorial(n1))
    elif m == 11:
        break
    time.sleep(2.5)
