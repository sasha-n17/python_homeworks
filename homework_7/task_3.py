class Cell:
    def __init__(self, num_of_cells):
        self.num_of_cells = num_of_cells

    def __str__(self):
        return str(self.num_of_cells)

    def __add__(self, other):
        return Cell(self.num_of_cells + other.num_of_cells)

    def __sub__(self, other):
        diff = self.num_of_cells - other.num_of_cells
        if diff > 0:
            return Cell(diff)
        else:
            return 'Разность количества ячеек отрицательна!'

    def __mul__(self, other):
        return Cell(self.num_of_cells * other.num_of_cells)

    def __truediv__(self, other):
        return Cell(self.num_of_cells // other.num_of_cells)

    def make_order(self, num_in_row):
        cells_in_rows_part_1 = ''.join(['*' * num_in_row + '\n' for _ in range(self.num_of_cells // num_in_row)])
        cells_in_rows_part_2 = ''.join(['*' * (self.num_of_cells % num_in_row)])
        return cells_in_rows_part_1 + cells_in_rows_part_2


cell_1 = Cell(20)
cell_2 = Cell(8)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(7))
