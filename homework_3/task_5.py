def calc_sum():
    """Возвращает сумму чисел из введённых строк. Q - спецсимвол для выхода."""
    result = 0
    flag = True
    while flag:
        s = input('Введите строку из чисел, разделённых пробелом: ').split()
        if 'Q' not in s:
            numbers = [float(el) for el in s]
            result += sum(numbers)

        else:
            pos = s.index('Q')
            numbers = [float(el) for el in s[:pos]]
            result += sum(numbers)
            flag = False
        print(f'Сумма чисел: {result}')
    return result


calc_sum()
