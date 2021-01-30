def my_func(time, rate, prize):
    salary = (time * rate) + prize
    return salary


print("Для рассчета заработной платы сотрудника через Edit Configurations, Terminal или cmd введите 3 параметра: количество отработанных часов, сумму ставки за 1 час и сумму премии.")
from sys import argv
try:
    name, a, b, c = argv
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        print(f"Заработная плата работника составляет {my_func(a, b, c)} у.е.")
    except ValueError:
        print("Как минимум один параметр не является числом. Введите корректные параметры и перезапустите программу.")
except:
    print("Вы ввели неправильное количество параметров (< 3 или > 3). Введите корректные параметры и перезапустите программу.")
