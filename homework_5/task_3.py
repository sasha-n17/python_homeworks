surnames = []
total, reference = 0, 20000
with open('task_3.txt', 'r+', encoding='utf-8') as f:
    info = [el.split() for el in f.readlines()]
    for el in info:
        total += float(el[1])
        if float(el[1]) < reference:
            surnames.append(el[0])
print(f"Список сотрудников, имеющих оклад менее {reference}: \n{', '.join(surnames)}")
print(f'Средняя величина дохода сотрудников: {round(total / len(info), 2)}')
