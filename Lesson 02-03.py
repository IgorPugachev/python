# Решение через list:

month = int(input("Введите номер месяца (1-12): "))
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
if month >= 1 and month <= 2 or month == 12:
    print(f"Данный месяц относится к времени года: {seasons[0]}")
elif month >= 3 and month <= 5:
    print(f"Данный месяц относится к времени года: {seasons[1]}")
elif month >= 6 and month <= 8:
    print(f"Данный месяц относится к времени года: {seasons[2]}")
elif month >= 9 and month <= 11:
    print(f"Данный месяц относится к времени года: {seasons[3]}")
else:
    print("Проверьте правильность введенной цифры")
    month = int(input("Enter month (1-12): "))

# Решение через dict

month = int(input("Введите номер месяца (1-12): "))
seasons = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень',
11: 'Осень', 12: 'Зима'}
if month in seasons.keys():
    print(f"Данный месяц относится к сезону: {seasons[month]}")
else:
    print("Проверьте правильность введенной цифры")


