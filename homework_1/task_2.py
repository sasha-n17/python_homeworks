time = int(input('Введите время в секундах: '))

hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

print(f'Время в формате hh:mm:ss: {hours}:{minutes}:{seconds}')
