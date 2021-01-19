import json

final_data = []

with open('task_7.txt', 'r+', encoding='utf-8') as f:
    firm_dict, average_dict = {}, {}
    total_profit, count = 0, 0
    for line in f:
        data_from_line = line.split()
        profit = float(data_from_line[2]) - float(data_from_line[3])
        firm_dict[data_from_line[0]] = profit
        if profit > 0:
            total_profit += profit
            count += 1
    average_dict['average_profit'] = round(total_profit / count, 2)
    final_data.append(firm_dict)
    final_data.append(average_dict)
print(final_data)

with open('task_7.json', 'w+', encoding='utf-8') as f:
    json.dump(final_data, f)
