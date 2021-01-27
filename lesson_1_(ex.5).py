gain = int(input("Укажите выручку фирмы: "))
cost = int(input("Укажите издержки фирмы: "))
if gain > cost:
    profit = gain - cost
    rent = profit / gain
    staff = int(input("Укажите численность сотрудников фирмы: "))
    p = profit / staff
    print(f"Фирма заработала {profit}. Рентабильность выручки составляет {rent:.2f}, прибыль фирмы в расчете на одного сотрудника составляет {p:.2f}.")
elif gain < cost:
    loss = gain - cost
    print(f"Убыток фирмы составляет {loss}.")
elif gain == cost:
    print("Фирма не заработала и не потратила.")