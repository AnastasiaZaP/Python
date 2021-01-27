def my_func(arg1, arg2, arg3):
    if max(arg1, arg2, arg3) == arg1:
        return f"Сумма наибольших двух аргументов = {arg1 + max(arg2, arg3)}"
    elif max(arg1, arg2, arg3) == arg2:
        return f"Сумма наибольших двух аргументов = {arg2 + max(arg1, arg3)}"
    elif max(arg1, arg2, arg3) == arg3:
        return f"Сумма наибольших двух аргументов = {arg3 + max(arg1, arg2)}"


print(my_func(float(input("Первый аргумент = ")), float(input("Второй аргумент = ")), float(input("Третий аргумент = "))))
