def personal_info(name, surname, year_of_birth, town, email, phone_number):
    info = [name, surname, year_of_birth, town, email, phone_number]
    return ' '.join(info)


print(personal_info(surname=input('Введите фамилию: '),
                    name=input('Введите имя: '),
                    town=input('Введите город: '),
                    phone_number=input('Введите номер телефона: '),
                    year_of_birth=input('Введите год рождения: '),
                    email=input('Введите адрес электронной почты: ')))


