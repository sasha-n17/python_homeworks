class IsDigit(Exception):
    def __init__(self, txt):
        self.txt = txt


output = []
flag = True
while flag:
    try:
        element = input('Введите число: ')
        if element == 'stop':
            flag = False
        if element.isdigit():
            output.append(float(element))
        else:
            raise IsDigit('Введено не число!')
    except IsDigit as error:
        print(error)
print(output)
