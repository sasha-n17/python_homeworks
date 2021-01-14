def division_func(var_1, var_2):
    try:
        var_1, var_2 = float(var_1), float(var_2)
        return var_1 / var_2
    except ValueError:
        print('Введено не число!')
    except ZeroDivisionError:
        print('Деление на ноль!')


try:
    a, b = input('Введите через пробел два числа: ').split()
    result = division_func(a, b)
    if result is not None:
        print(f'Результат деления числа {a} на число {b} = {result}')
except ValueError:
    print('Некорректный ввод. Недостаточно или слишком много значений для распаковки')
