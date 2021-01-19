info_dict = {}
with open('task_6.txt', 'r+', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        position = line.find(':')
        subject, values_list = line[:position], line[position+1:].split()
        total = 0
        for el in values_list:
            if el != '—':
                total += int(el[:el.find('(')])
        info_dict[subject] = total
print(info_dict)
