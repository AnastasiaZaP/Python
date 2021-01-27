def questionnaire(name, surname, year, city, email, phone):
    # print(f"Ваши данные: {name} {surname}, {year}, {city}, {email}, {phone}")
    return f"Ваши данные: {name} {surname}, {year}, {city}, {email}, {phone}"

print(questionnaire(email=input("Введите ваш email: "), phone=input("Введите ваш телефон: "), name=input("Введите ваше имя: "), surname=input("Введите вашу фамилию: "), year=input("Введите год вашего рождения: "), city=input("Введите город проживания: ")))
