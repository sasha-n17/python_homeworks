class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости!'
        else:
            return Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости!'
        else:
            return Car.show_speed(self)


class PoliceCar(Car):
    pass


car_1 = SportCar(100, 'white', 'BMW', False)
print(car_1.name)
print(car_1.color)
print(car_1.speed)
print(car_1.is_police)
print(car_1.go())
print(car_1.stop())
print(car_1.go())
print(car_1.turn('налево'))
print(car_1.show_speed())
print('-----------')

car_2 = TownCar(70, 'grey', 'BMW', False)
print(car_2.name)
print(car_2.color)
print(car_2.speed)
print(car_2.is_police)
print(car_2.go())
print(car_2.stop())
print(car_2.go())
print(car_2.turn('направо'))
print(car_2.show_speed())
print('-----------')

car_3 = WorkCar(50, 'black', 'BMW', False)
print(car_3.name)
print(car_3.color)
print(car_3.speed)
print(car_3.is_police)
print(car_3.go())
print(car_3.stop())
print(car_3.go())
print(car_3.turn('налево'))
print(car_3.show_speed())
print('-----------')

car_4 = PoliceCar(90, 'blue', 'Ford', True)
print(car_4.name)
print(car_4.color)
print(car_4.speed)
print(car_4.is_police)
print(car_4.go())
print(car_4.stop())
print(car_4.go())
print(car_4.turn('назад'))
print(car_4.show_speed())
