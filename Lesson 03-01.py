def division(*args):
    try:
        dividend = int(input("Введите делимое: "))
        divisor = int(input("Введите делитель: "))
        res = dividend / divisor

    except ValueError:
        return "Проверьте правильность введенного числа"
    except ZeroDivisionError:
        return "Деление на ноль!"

    return res

print(f"Результат деления: {division()}")

