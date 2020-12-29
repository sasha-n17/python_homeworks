n = int(input('Введите количество элементов в списке: '))

test_list = [input('Введите элемент: ') for i in range(n)]
print(f'Список до обмена: {test_list}. Длина списка: {n}.')
if n % 2 == 0:
    for i in range(0, n, 2):
        test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
    print(f'Список после обмена: {test_list}')
else:
    print(f'Так как длина списка нечётная, последний элемент сохранит свою позицию.')
    for i in range(0, n-1, 2):
        test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
    print(f'Список после обмена: {test_list}')
