test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
answer = [el for el in test_list if test_list.count(el) == 1]
print(answer)
