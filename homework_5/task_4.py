rus_eng_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = ''
with open('task_4.txt', 'r', encoding='utf-8') as f_src:
    for line in f_src:
        src_line = line.strip('\n')
        numeral = src_line[:src_line.find('—') - 1]
        new_text += src_line.replace(numeral, rus_eng_dict[numeral]) + '\n'

with open('task_4_upd.txt', 'w+', encoding='utf-8') as f_target:
    f_target.write(new_text)
