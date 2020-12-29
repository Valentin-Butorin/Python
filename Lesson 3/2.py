def collect_user_info(*args):
    return args


firstname = 'Иван'
lastname = 'Иванов'
year_of_birth = 1991
city = 'Иркутск'
email = 'mail@mail.ru'
phone_number = 88005553535
print(*collect_user_info(firstname, lastname, year_of_birth, city, email, phone_number))
