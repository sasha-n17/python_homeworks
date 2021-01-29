class IncorrectDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    num_1, num_2 = [float(el) for el in input('Введите через пробел два числа: ').split()]
    if num_2 == 0:
        raise IncorrectDivision('Деление на ноль!')
    print(f'Результат деления {num_1} на {num_2} = {num_1 / num_2}')
except IncorrectDivision as error:
    print(error)
except ValueError:
    print('Некорректный ввод!')
