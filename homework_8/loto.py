from random import randint, choice


class Card:
    def __init__(self, player):
        self.player = player
        self.__matrix_numbers = []
        self.__matrix_card = []
        self.generate_numbers()
        self.fill_the_card()

    def __str__(self):
        print(f'Карточка игрока: {self.player}')
        output = '-' * 18 + '\n'
        i = 0
        for row in self.__matrix_card:
            output += ' '.join([str(el) for el in self.__matrix_card[i]]) + '\n'
            i += 1
        output += '-' * 18
        return output

    def generate_numbers(self):
        numbers_in_card = set()
        for i in range(3):
            numbers_in_row = set()
            while len(numbers_in_row) != 5:
                num = randint(1, 90)
                if num not in numbers_in_card:
                    numbers_in_row.add(num)
            numbers_in_card.update(numbers_in_row)
            self.__matrix_numbers.append(sorted(list(numbers_in_row)))
        return 'Генерация чисел для карточки завершена'

    def fill_the_card(self):
        for i in range(3):
            pos_in_row = set()
            while len(pos_in_row) != 5:
                num = randint(0, 8)
                if num not in pos_in_row:
                    pos_in_row.add(num)
            matrix_row = ['' for _ in range(9)]
            pos_in_row_sorted = sorted(list(pos_in_row))
            for j in range(len(pos_in_row_sorted)):
                matrix_row[pos_in_row_sorted[j]] = self.__matrix_numbers[i][j]
            self.__matrix_card.append(matrix_row)

    def check_number(self, num):
        for row in self.__matrix_card:
            if num in row:
                position = row.index(num)
                row[position] = '-'
                break

    def exist_numbers(self):
        for row in self.__matrix_card:
            if ''.join([str(el) for el in row]).isalnum():
                return True
        return False


class BagOfBarrel:
    def __init__(self):
        self.quantity = 90
        self.__numbers_in_bag = [i for i in range(1, 91)]

    def generate_num_of_barrel(self):
        num = choice(self.__numbers_in_bag)
        self.__numbers_in_bag.remove(num)
        return num


# настройки игры
# Шанс, что компьютер сделает неправильный ход (0 - компьютер не ошибается).
mistake_choice = 0

# создаём карточки игроков
player_1 = Card('Александр')
player_2 = Card('Компьютер')

# создаём мешок с бочонками
bag_of_barrel = BagOfBarrel()

while player_1.exist_numbers() and player_2.exist_numbers():
    print(player_1)
    print(player_2)
    print(f'Номер из бочонка {bag_of_barrel.generate_num_of_barrel()}')
    input_from_user = input('Зачеркнуть номер? д / н: ')
