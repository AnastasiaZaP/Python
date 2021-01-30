def fact(factorial):
    for tek_num in range(0, factorial + 1):
        if factorial == 0 or tek_num == 1:
            tek_fact = 1
            yield tek_fact
        elif tek_num == 0:
            tek_fact = 1
        else:
            tek_fact *= tek_num
            yield tek_fact


while True:
    try:
        n = int(input("Введите целое неотрицательное число n для расчёта n!: "))
        if n < 0:
            print("Введенное число должно быть неотрицательным. Попробуйте еще раз.")
        else:
            break
    except ValueError:
        print("Вы должны ввести целое число. Попробуйте еще раз.")
for el in fact(n):
    print(el)
