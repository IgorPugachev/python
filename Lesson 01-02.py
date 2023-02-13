time_input = int(input("Введите время в секундах: "))

time_hours = int(time_input//3600)
time_minutes = (time_input - time_hours*3600)//60
time_seconds = time_input - (time_hours*3600 + time_minutes*60)
print(f"Время в формате чч:мм:сс: {time_hours}:{time_minutes}:{time_seconds}")

