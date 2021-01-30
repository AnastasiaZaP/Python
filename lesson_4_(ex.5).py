from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, list(i for i in range(100, 1001, 2))))

# более простое решение
# my_list = []
# for i in range(100, 1001, 2):
#     my_list.append(i)
# proizvedenie = 1
# for j in my_list:
#     proizvedenie *= j
# print(proizvedenie)
