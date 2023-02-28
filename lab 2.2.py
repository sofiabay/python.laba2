number = int(input'Укажите номер места в плацкартном вагоне'))
if (number > 35):
    print('Такого номера не существует, проверьте данные')
    import sys
    sys.exit(0)
elif (number > 0 and number < 17):
    print("Ваше место в купе")
else:
    print("Ваше место - боковое")
if (number % 2 == 0):
    print(", верхнее место")
else:
    print(", нижнее место")

