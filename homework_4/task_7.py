from math import factorial


def fact(n):
    for number in range(1, n + 1):
        yield number, factorial(number)


for el in fact(int(input('Введите число: '))):
    print(f'{el[0]}! = {el[1]}')
