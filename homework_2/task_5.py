my_list = [7, 5, 3, 3, 2]

N = int(input('Введите количество итераций ввода нового элемента рейтинга: '))
for i in range(N):
    number = int(input('Введите новый элемент рейтинга: '))
    if number in set(my_list):
        pos = my_list[-1::-1].index(number)
        my_list.insert(len(my_list) - pos, number)
        print(my_list)
    elif number > my_list[0]:
        my_list.insert(0, number)
        print(my_list)
    elif number < my_list[-1]:
        my_list.append(number)
        print(my_list)
    else:
        for j in range(1, len(my_list) - 1):
            if number > my_list[j]:
                my_list.insert(j, number)
                print(my_list)
                break
            else:
                j += 1
