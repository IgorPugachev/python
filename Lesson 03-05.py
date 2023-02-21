def my_sum ():
    sum_res = 0
    check = False
    while not check:
        number = input('Введите строку чисел, разделенных пробелом или введите Q чтобы выйти - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                check = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Окончательная сумма:  {sum_res}')

my_sum()
