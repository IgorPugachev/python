from functools import reduce

def my_func(el_prev, el):
    return el_prev * el

print(f'Список четных значений списка от 100 до 1000: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всх элементов списка {reduce(my_func, [el for el in range(99,1001) if el % 2 == 0])}')

