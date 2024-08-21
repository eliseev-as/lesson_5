number = int(input("Введите целое число: "))

rem = number % 2

if number == 0:
    print("Нулевое число")
elif number > 0:
    if rem == 0:
        print("Положительное четное число")
    else:
        print("Положительное нечетное число")
else:
    if rem == 0:
        print("Отрицательное четное число")
    else:
        print("Отрицательное нечетное число")
