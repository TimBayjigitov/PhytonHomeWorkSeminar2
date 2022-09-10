# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

def DigitSum(num):
    suma = 0
    minus = '-'
    if minus not in num:
        for digit in num:
         if digit.isdigit():
            suma += int(digit)

    else:
        a = num[1]
        for digit in num:
            if digit.isdigit():
                suma += int(digit)
        suma = suma - int(a) * 2
    return suma
digit = list(input(f"{'Введите вещественное число: '}"))
print(f'Сумма введенного вещестного числа = {DigitSum(digit)}')



