from itertools import count, cycle

# итератор, генерирующий целые числа, начиная с указанного
try:
    n = int(input('Введите число: '))
    for el in count(n):
        if el <= 2 * n:
            print(el)
        else:
            break
except ValueError:
    print('Введено не число!')

print()

# итератор, повторяющий элементы некоторого списка, определённого заранее
test_list = list('PYTHON')
c = 0
for el in cycle(test_list):
    if c >= 2 * len(test_list):
        break
    print(el)
    c += 1
