text = input('Введите строку из нескольких слов, разделённых пробелами: ')

print(f'Количество слов в введённой строке: {len(text.split())}')
for i, el in enumerate(text.split()):
    print(f'{i+1}. {el[:10]}')
