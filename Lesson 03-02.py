def user_data(name, surname, birthyear, city_living, email, phone):
    return ' '.join([name, surname, birthyear, city_living, email, phone])

print(user_data(name = 'Ivan', surname = 'Petrov', birthyear = '1983', city_living = 'Melbourne', email = 'petrov@gmail.com', phone = '0450-345-213'))
