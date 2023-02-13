a = int(input("Введите результат в километрах в первый день тренировок: "))
b = int(input("Введите целевой показатель в километрах: "))

result_days = 1
result_km = a
while result_km < b:
    a = a + a*0.1
    result_days += 1
    result_km = a
print(f"Вы достигнете требуемых показателей на {result_days:d} день")
