products = []
analysis_dict = {'название': [],
                 'цена': [],
                 'количество': [],
                 'ед': set()}

N = int(input('Введите сколько товаров нужно внести: '))
for i in range(N):
    info = input('Введите название, цену, количество и единицу измерения товара. '
                 'Данные параметры перечислите через запятую и пробел: ')
    info_list = info.split(', ')
    info_dict = {'название': info_list[0],
                 'цена': int(info_list[1]),
                 'количество': int(info_list[2]),
                 'ед': info_list[3]}
    products.append((i + 1, info_dict))
    analysis_dict['название'].append(info_list[0])
    analysis_dict['цена'].append(int(info_list[1]))
    analysis_dict['количество'].append(int(info_list[2]))
    analysis_dict['ед'].add(info_list[3])

print('---------------------------------------------------------------------')
print('Структура данных "Товары" выглядит следующим образом:')
for row in products:
    print(row)
print('---------------------------------------------------------------------')
print('Аналитика о товарах выглядит следующим образом:')
for key, item in analysis_dict.items():
    print(key, ':', item)
print('---------------------------------------------------------------------')
