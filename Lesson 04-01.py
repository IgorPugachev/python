from sys import argv

name, time, salary, bonus = argv
try:
    name = input("Укажите имя сотрудника: ")
    time = int(input("Укажите рабочее время в часах: "))
    salary = int(input("Укажите ставку в час: "))
    bonus = int(input("Укажите размер бонуса: "))
    result = time * salary + bonus
    print(f'Заработная плата {name} составляет: {result}')
except ValueError:
    print("Это не число")
