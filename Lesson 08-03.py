class NotNumberError(Exception):
    pass

# создаем метод
def get_numbers():
# создаем пустой список, куда будут добавляться вводимые нами числа
    numbers = []
# создаем бесконечный цикл While (выход из него будет по слову stop)
    while True:
# используем конструкцию try-except
        try:
# запрашиваем у пользователя ввод числа
            user_input = input('Введите число: ')
# если пользователь введет слово stop, цикл прервется
# и система выведет списое тех значений, которые были введены до слова stop
# если до этого ничего не было введено, система покажет пустой список
            if user_input == 'stop':
                break
# вводимое пользователем число переводится в формат float number (даже не помню,
# как это сказать по-русски. Этот формат будет определять число десятичных знаков в числе
            number = float(user_input)
# встроенная функция проверяет, что введенная информация является числом
            if not isinstance(number, (int, float)):
# если нет - вызывается встроенный метод NoNumberError (показ ошибки при вводе не числа)
                raise NotNumberError(f'{number} не является числом')
            numbers.append(number)
        except ValueError:
            print('Вы ввели не число. Попробуйте снова.')
        except NotNumberError as e:
            print(e)
    return numbers


if __name__ == '__main__':
    numbers = get_numbers()
    print(numbers)
