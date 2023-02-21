
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""
def my_func(arg1, arg2, arg3):
    if arg3 >= arg1 and arg2 >= arg1:
        return arg3 + arg2
    elif arg1 > arg3 and arg2 > arg3:
        return arg1 + arg2
    else:
        return arg1 + arg3

print(f'Результат сложения - {my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))}')



