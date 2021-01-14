def int_func(word):
    if word.islower() and word.isalpha():
        return word.title()
    else:
        print('Некорректный ввод.')


s = input('Введите одно слово из маленьких латинских букв: ')
if int_func(s) is not None:
    print(int_func(s))
