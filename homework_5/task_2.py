with open('task_2.txt', 'r+', encoding='utf-8') as f:
    info = f.readlines()
    print(f'Количество строк в файле: {len(info)}')
    for i, el in enumerate(info):
        print(f'{i + 1} строка. Количество слов: {len(el.split())}')
