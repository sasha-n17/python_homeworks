class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        income = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


person_1 = Position('Ivan', 'Ivanov', 'менеджер', 10000, 5000)
print(person_1.name)
print(person_1.surname)
print(person_1.position)
print(person_1.get_full_name())
print(person_1.get_total_income())
print('-----------')
person_2 = Position('Петр', 'Петров', 'разработчик', 20000, 10000)
print(person_2.name)
print(person_2.surname)
print(person_2.position)
print(person_2.get_full_name())
print(person_2.get_total_income())
