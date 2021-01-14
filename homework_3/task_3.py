def my_func(var_1, var_2, var_3):
    try:
        variables = [float(el) for el in [var_1, var_2, var_3]]
        max_1, max_2 = sorted(variables, reverse=True)[0:2]
        return max_1 + max_2
    except ValueError:
        print('Введено не число!')


try:
    a, b, c = input('Введите через пробел три числа: ').split()
    result = my_func(a, b, c)
    if result is not None:
        print(f'Сумма наибольших двух аргументов среди {float(a)}, {float(b)}, {float(c)} = {result}')
except ValueError:
    print('Некорректный ввод. Недостаточно или слишком много значений для распаковки')
