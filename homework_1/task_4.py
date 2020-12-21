n = int(input('Введите целое положительное число n: '))

max_number = 0
while n % 10 != 0:
    if n % 10 > max_number:
        max_number = n % 10
    n //= 10
print(f'Самая большая цифра в числе: {max_number}')
