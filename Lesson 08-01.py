"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Date:
# класс будет иметь три параметра
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
# создаем метод (с декоратором @classmethod), преобразующий в число
# введенную нами дату.
    @classmethod
    def from_string(cls, date_string):
# сначала метод split() обрабатывает строку по разделителю (в данном случае это знак "тире")
# и возвращает список строк.
# затем метод map() проходит по каждому элементу в списке
# и преобразовывает его в число
# а метод класса вызывает метод __init__ класса Date,
# чтобы создать новый экземпляр класса с указанными значениями атрибутов.
        day, month, year = map(int, date_string.split("-"))
        return cls(day, month, year)

# а этот метод проверяет правильность формата вводимых для даты данных
    @staticmethod
    def is_valid_date(date_string):
        day, month, year = map(int, date_string.split("-"))
# проверка, что номер месяца находится в разрешенных пределах (1-12)
        if month < 1 or month > 12:
            return False
# проверка, что число дня находится в разрешенных пределах (1-31)
        if day < 1 or day > 31:
            return False
# проверка, что число дней не превышает 30 в тех месяцах, где 30 дней
        if month in [4, 6, 9, 11] and day > 30:
            return False
# проверка, что количество дней для февраля не превышает 29
        if month == 2:
            if day > 29:
                return False
# и проверка на високосный год
            if day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                return False
        return True

# Пример использования класса

date_string = "30-02-2023"

if Date.is_valid_date(date_string):
    date = Date.from_string(date_string)
    print(f"День: {date.day}")
    print(f"Месяц: {date.month}")
    print(f"Год: {date.year}")
else:
    print("Некорректная дата")
