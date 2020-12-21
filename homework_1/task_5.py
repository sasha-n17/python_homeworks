proceeds = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))

if proceeds > costs:
    print('Финансовый результат фирмы - прибыль')
    profit = proceeds - costs
    profitability = profit / proceeds
    print(f'Рентабельность выручки составила: {profitability}')
    numbers = int(input('Введите количество сотрудников в фирме: '))
    profit_emp = profit / numbers
    print(f'Прибыль на одного сотрудника в фирме составляет: {profit_emp}')
elif proceeds == costs:
    print('Фирма имеет одинаковые показатели выручки и издержек')
else:
    print('Финансовый результат фирмы - убыток')
    loss = costs - proceeds
    print(f'Убыток фирмы составил {loss}')
