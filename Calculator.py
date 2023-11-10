import math
import time

def main():
    l = ['1. Сложить 2 числа', '2. Вычесть второе из первого', '3. Перемножить два числа',
         '4. Разделить первое на второе', '5. Возвести в степень N первое число', '6. Найти квадратный корень из числа',
         '7. Найти факториал', '8. Найти синус', '9. Найти косинус', '10. Найти тангенс', '11. Плозадь треугольника', '12. Проверка на четность', '13. Сумма цифр числа', '14. ВЫХОД']
    for j in l:
        print(j)

def rectangle_area(weight, height):
    return (math.sqrt(weight**2 + height**2))

def is_even(number):
    return number%2 == 0

def sum_digits(numbers):
    sum = 0
    while numbers > 0:
        sum += numbers % 10
        numbers = numbers // 10
    return sum

while True:
    main()
    m = input("Введите действие ")
    try:
        m = int(m)
    except:
        print("Вы ввели некорректное действие")
        continue
    if m > 14 or m < 1:
        print("Вы ввели некорректное действие")
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
            try:
                print(math.sqrt(n1))
            except:
                print("Вы ввели некорректные данные")
                continue
        elif m == 8:
            print(math.sin(math.radians(n1)))
        elif m == 9:
            print(math.cos(math.radians(n1)))
        elif m == 10:
            print(math.tan(math.radians(n1)))
    elif m == 7:
        try:
            n1 = int(input("Введите число "))
            math.factorial(n1)
        except:
            print("Вы ввели некорректные данные")
            continue
        print(math.factorial(n1))
    elif m == 11:
        try:
            n1 = int(input("Введите первое число "))
            n2 = int(input("Введите второе число "))
        except:
            print("Вы ввели некорректные данные")
            continue
        print(rectangle_area(n1, n2))
    elif m == 12:
        try:
            n1 = int(input("Введите число "))
        except:
            print("Вы ввели некорректные данные")
            continue
        print(is_even(n1))
    elif m == 13:
        try:
            n1 = int(input("Введите число "))
        except:
            print("Вы ввели некорректные данные")
            continue
        print(sum_digits(n1))
    elif m == 14:
        break
    time.sleep(2.5)

