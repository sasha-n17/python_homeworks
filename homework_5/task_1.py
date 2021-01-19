with open('task_1.txt', 'w+', encoding='utf-8') as f:
    while True:
        input_user = input('Введите что-нибудь: ')
        if len(input_user) > 0:
            f.write(input_user + '\n')
        else:
            break
