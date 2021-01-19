class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title} ручкой!'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title} карандашом!'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title} маркером!'


test_1 = Stationery('картинки')
print(test_1.draw())
test_2 = Pen('картинки')
print(test_2.draw())
test_3 = Pencil('картинки')
print(test_3.draw())
test_4 = Handle('картинки')
print(test_4.draw())
