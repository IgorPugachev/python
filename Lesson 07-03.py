# Создаем класс Cell, представляющий клетку, которая содержит
# определенное количество ячеек (параметр num_cells)
# Определяем для этого класса несколько методов для выполнения математических операций с клетками,
# а также метод make_order для форматированного вывода ячеек в ряды.
class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells
# метод __add__ определяет оператор сложения (+) для клеток,
# который возвращает новую клетку с количеством ячеек,
# равным сумме ячеек двух клеток, переданных оператору.

    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

# Метод __sub__ определяет оператор вычитания (-) для клеток,
# который возвращает новую клетку с количеством ячеек,
# равным разности ячеек двух клеток, переданных оператору, если разность больше 0.
# Если же разность меньше или равна 0, то выводится сообщение об ошибке.

    def __sub__(self, other):
        result = self.num_cells - other.num_cells
        if result > 0:
            return Cell(result)
        else:
            print('Разность количества ячеек двух клеток меньше или равна нулю')

# Метод __mul__ определяет оператор умножения (*) для клеток,
# который возвращает новую клетку с количеством ячеек,
# равным произведению ячеек двух клеток, переданных оператору.

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

# Метод __truediv__ определяет оператор деления (/) для клеток,
# который возвращает новую клетку с количеством ячеек,
# равным целочисленному делению ячеек двух клеток, переданных оператору.

    def __truediv__(self, other):
        return Cell(self.num_cells // other.num_cells)

# Метод make_order принимает аргумент num_cells_per_row - количество ячеек в ряду,
# и возвращает строку, содержащую ряды ячеек, разбитых на группы по num_cells_per_row.
# Если количество ячеек в клетке не делится нацело на num_cells_per_row,
# то последний ряд будет содержать меньше ячеек.

    def make_order(self, num_cells_per_row):
        num_rows = self.num_cells // num_cells_per_row
        remainder = self.num_cells % num_cells_per_row
        rows = ['*' * num_cells_per_row for i in range(num_rows)]
        if remainder:
            rows.append('*' * remainder)
        return '\n'.join(rows)


# Пример использования:
cell1 = Cell(10)
cell2 = Cell(5)

# Сложение
cell3 = cell1 + cell2
print(cell3.num_cells)  # 15

# Вычитание
cell4 = cell1 - cell2
print(cell4.num_cells)  # 5

cell5 = cell2 - cell1  # Разность количества ячеек двух клеток меньше или равна нулю

# Умножение
cell6 = cell1 * cell2
print(cell6.num_cells)  # 50

# Деление
cell7 = cell1 / cell2
print(cell7.num_cells)  # 2

cell8 = cell2 / cell1
print(cell8.num_cells)  # 0

# make_order
cell9 = Cell(12)
print(cell9.make_order(5))
# *****
# *****
# **

cell10 = Cell(15)
print(cell10.make_order(5))
# *****
# *****
# *****