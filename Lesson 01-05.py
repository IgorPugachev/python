turnover = int(input("Введите цифру выручки: "))
costs = int(input("Введите цифру издержек: "))

fin_result = turnover - costs
if fin_result > 0:
    print(f"Firm profit is: {fin_result} рублей")
elif fin_result < 0:
    print(f"Убытки фирмы: {fin_result} рублей")
else:
    print("Фирма работает с нулевым результатом")