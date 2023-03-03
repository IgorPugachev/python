# создаем класс Matrix
class Matrix:
# загружаем конструктор класса (метод __init__)
    def __init__(self, data):
        self.data = data
# загружаем метод __str__
    def __str__(self):
# создаем пустой список rows
        rows = []
# используя for cycle, делаем обход этого списка, беря данные для него из параметров атрибута data, созданного до этого
# Метод __str__ формирует строковое представление матрицы,
# разделяя элементы в строках табуляцией и строки переносом строки.
        for row in self.data:
            row_str = "\t".join(str(val) for val in row)
            rows.append(row_str)
        return "\n".join(rows)
# Метод __add__ реализует сложение матриц покомпонентно.
# Перед сложением проверяется, что матрицы имеют одинаковые размеры,
# в случае, если это не так, возникает исключение ValueError.
# В результате сложения создается новый объект класса Matrix, содержащий сумму матриц.
    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Matrices must have the same number of rows")
        if len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same number of columns")

        result = []
        for i in range(len(self.data)):
            result_row = []
            for j in range(len(self.data[0])):
                result_row.append(self.data[i][j] + other.data[i][j])
            result.append(result_row)
        return Matrix(result)

# передаем следующий список списков в конструктор класса:
data = [[1, 2, 3], [4, 5, 6]]
mat = Matrix(data)
print(mat)

# Также можно создать матрицу из списка в виде строки, разделенной пробелами
# и символами новой строки. Для этого нужно сначала разбить строку на строки матрицы,
# затем каждую строку разбить на элементы и преобразовать их в числа. Например:

data_str = "1 2 3\n4 5 6"
data = [[int(val) for val in row.split()] for row in data_str.split("\n")]
matrix = Matrix(data)
print(matrix)