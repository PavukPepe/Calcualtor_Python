import math
import time
while True:
    l = ['1. Сложить 2 числа', '2. Вычесть второе из первого', '3. Перемножить два числа', '4. Разделить первое на второе', '5. Возвести в степень N первое число', '6. Найти квадратный корень из числа', '7. Найти факториал', '8. Найти синус', '9. Найти косинус', '10. ВЫХОД']
    for j in l:
        print(j)
        time.sleep(0.2)
    m = input("Введите действие ")
    if m.isdigit():
        m = int(m)
    else:
        print("Некорректное значние")
        continue
    if m == 1 or m == 2 or m == 3 or m == 4:
        n1 = input("Введите первое число ")
        n2 = input("Введите второе число ")
        if n1.isdigit() and n2.isdigit():
            n1 = int(n1)
            n2 = int(n2)
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
        else:
            print("Вы ввели не число")
    elif m == 5:
        n1 = input("Введите первое число ")
        n2 = input("Введите степень ")
        if n1.isdigit() and n2.isdigit():
            n1 = int(n1)
            n2 = int(n2)
            print(math.pow(n1, n2))
        else:
            print("Вы ввели не число")
    elif m == 6 or m == 7 or m == 8 or m == 9:
        n1 = input("Введите число ")
        if n1.isdigit():
            n1 = int(n1)
            if m == 6:
                print(math.sqrt(n1))
            elif m == 7:
                print(math.factorial(n1))
            elif m == 8:
                print(math.sin(n1))
            elif m == 9:
                print(math.cos(n1))
        else:
            print("Вы ввели не число")
    elif m == 10:
        break
    time.sleep(2.5)
