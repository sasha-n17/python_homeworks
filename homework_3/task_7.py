def int_func(text):
    test = ''.join(text.split())
    if test.islower() and test.isalpha():
        return text.title()
    else:
        print('Некорректный ввод.')


s = input('Введите строку, состоящую из слов в нижнем регистре, разделённых пробелами: ')
if int_func(s) is not None:
    print(int_func(s))
