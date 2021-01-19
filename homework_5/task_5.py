with open('task_5.txt', 'w+', encoding='utf-8') as f:
    f.write(input('Введите набор чисел, разделённых пробелом: '))

with open('task_5.txt', 'r+', encoding='utf-8') as f:
    numbers = f.readline()
    try:
        if len(numbers) > 0:
            print(f'Сумма чисел в файле: {sum([float(el) for el in numbers.split()])}')
        else:
            print('Файл пуст, нет чисел для подсчёта!')
    except ValueError:
        print('Некорректный ввод!')
