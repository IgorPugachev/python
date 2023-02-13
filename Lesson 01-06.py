turnover = int(input("Введите цифру выручки в рублях: "))
costs = int(input("Введите цифру издержек в рублях: "))

fin_result = turnover - costs
if fin_result > 0:
    profitability = ((fin_result/costs)*100)
    print(f"Прибыльность фирмы: {profitability}%")
    staff = int(input("Сколько сотрудников в фирме?"))
    profit_per_staff = fin_result/staff
    print(f"Прибыль фирмы в расчете на одного сотрудника: {profit_per_staff} рублей в год")
elif fin_result < 0:
    print(f"Убытки фирмы: {fin_result} рублей")
else:
    print("Фирма работает с нулевой прибылью")