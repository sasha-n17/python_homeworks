from sys import argv

if 'h' in argv:
    print('Расчёт заработной платы сотрудника.Введите выработку в часах, ставку в час и премию')
else:
    working_hours, rate_per_hour, bonus = argv[1:]
    salary = float(rate_per_hour) * float(working_hours) + float(bonus)
    print('Выработка в часах:', working_hours)
    print('Ставка в час:', rate_per_hour)
    print('Премия:', bonus)
    print('Зарплата:', salary)
