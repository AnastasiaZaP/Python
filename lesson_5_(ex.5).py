import random
my_list = list(random.randint(5, 40) for i in range(10))
with open("numbers.txt", "w+", encoding="utf-8") as my:
    for el in range(len(my_list)):
        if el == 0:
            my.write(str(my_list[el]))
        else:
            my.write(" " + str(my_list[el]))
    my.seek(0)
    a = my.read().split()
    sum_num = 0
    for el in a:
        sum_num += int(el)
    print(f"Сумма чисел в файле = {sum_num}")
