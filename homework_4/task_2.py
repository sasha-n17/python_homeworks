test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [el for i, el in enumerate(test_list) if test_list[i] > test_list[i - 1] and i > 0]
print(res_list)
