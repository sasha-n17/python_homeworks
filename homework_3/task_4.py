# реализация через **
def my_func1(x, y):
    try:
        x, y = float(x), int(y)
        return x ** y
    except ValueError:
        print('Введено не число или указана нецелая степень')
    except ZeroDivisionError:
        print('Ноль нельзя возводить в отрицательную степень! Возникает деление на 0.')


# реализация через цикл
def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if y == 0:
            return 1
        else:
            result = x
            for i in range(abs(y)-1):
                result *= x
            if y >= 0:
                return result
            else:
                return 1 / result
    except ValueError:
        print('Введено не число или указана нецелая степень')
    except ZeroDivisionError:
        print('Ноль нельзя возводить в отрицательную степень! Возникает деление на 0.')


try:
    a, b = input('Введите через пробел два числа: ').split()
    result1 = my_func1(a, b)
    result2 = my_func2(a, b)
    if result1 is not None and result2 is not None:
        print(f'Реализация через **. Возведение числа {a} в степень {b} = {result1}')
        print(f'Реализация через цикл. Возведение числа {a} в степень {b} = {result2}')
except ValueError:
    print('Некорректный ввод. Недостаточно или слишком много значений для распаковки')
