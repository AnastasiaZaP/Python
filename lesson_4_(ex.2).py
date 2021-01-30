# Проба на примере исходного списка
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[el] for el in range(len(my_list)) if my_list[el] > my_list[el-1] and el > 0]
print(new_list)

# Решение с генератором исходного списка
import random
my_list = list(random.randint(0,300) for i in range(13))
print(my_list)
new_list = [my_list[el] for el in range(len(my_list)) if my_list[el] > my_list[el-1] and el > 0]
print(new_list)