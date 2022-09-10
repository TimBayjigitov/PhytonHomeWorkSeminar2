# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

def InvertNum(num):
    inverted = 0
    while num != 0:
            inverted = inverted * 10 + (num % 10)
            num //= 10
    return inverted

def FindPolindrom(InvertedNum, num):
    polindrom = InvertedNum + num
    if num == InvertedNum:
        print(f'Ваше число {num} и есть полиндром')
    elif num != InvertedNum:
        while polindrom != InvertNum(polindrom):
            polindrom += InvertNum(polindrom)
    return polindrom
n = InputNumbers('Введите число: ')
inverted = InvertNum(n)
print(f'полиндром введеного числа {n} --> {FindPolindrom(inverted,n)}')



