from itertools import count

for el in count(int(input('Введите стартовое число:'))):
    print(el)

from itertools import cycle

my_list = ['FSE', True, None, 789]
for el in cycle(my_list):
    print(el)
