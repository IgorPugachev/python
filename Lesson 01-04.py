user_number = int(input("Введите целое положительное число: "))

max_number = 0
while user_number != 0:
    current_number = user_number % 10
    if max_number < current_number:
        max_number = current_number
        user_number = user_number // 10
    else:
        break

print(f"Самая большая цифра в числе: {max_number}")
