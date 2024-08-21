minimum_amount_investments = int(input("Введите минимальную сумму инвестиций: "))
mike = int(input("Введите количество доларов у Майкла: "))
ivan = int(input("Введите количество доларов у Ивана: "))

if mike >= minimum_amount_investments and ivan >= minimum_amount_investments:
    print(2)
elif mike >= minimum_amount_investments:
    print('Mike')
elif ivan >= minimum_amount_investments:
    print('Ivan')
elif mike + ivan >= minimum_amount_investments:
    print(1)
else:
    print(0)
