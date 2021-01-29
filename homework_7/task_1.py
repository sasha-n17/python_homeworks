def input_matrix():
    n, m = [int(el) for el in input('Введите количество строк и столбцов в вводимой матрице: ').split()]
    output_matrix = []
    for i in range(n):
        print(f'Ввод {i + 1} строки матрицы')
        while True:
            input_line = [float(el) for el in input(f'Введите через пробел {m} числа/чисел: ').split()]
            if len(input_line) != m:
                print(f'Количество чисел в строке отличается от ожидаемого, '
                      f'введено {len(input_line)}, ожидалось {m}')
            else:
                break
        output_matrix.append(input_line)
    return output_matrix


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        self.__matrix_output = ''
        for row in self.my_list:
            self.__matrix_output += '   '.join([str(el) for el in row]) + '\n'
        return self.__matrix_output

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list) and len(self.my_list[0]) == len(other.my_list[0]):
            my_list_res = [[0 for _ in range(len(self.my_list[0]))] for _ in range(len(self.my_list))]
            for row in range(len(other.my_list)):
                for col in range(len(other.my_list[0])):
                    my_list_res[row][col] = self.my_list[row][col] + other.my_list[row][col]
            return Matrix(my_list_res)
        else:
            return 'Размеры матриц не совпадают. Сложение матриц невозможно!\n'


matrix = Matrix([[31, 22], [37, 43], [51, 86]])
print(matrix)
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix_2)
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matrix_3)
matrix_4 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix + matrix_4)
print(matrix + matrix_2)
print(matrix + matrix_4 + matrix)

# реализация ввода матрицы произвольного размера пользователем для создания экземпляра класса
test_matrix = Matrix(input_matrix())
print(test_matrix)
