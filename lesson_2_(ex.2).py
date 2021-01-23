my_list = []
my_list_reverse = []
my_list = list(input("Введите элементы списка: "))

# 1-й способ
print(f"Список состоит из элементов: {my_list}")
for el in range(len(my_list)):
    if el % 2 == 0:
        a = my_list[el:el+2][::-1]
        my_list_reverse.extend(a)

# 2-й способ
#for el in range(0,len(my_list),2):
    # a = my_list[el:el + 2][::-1]
    # my_list_reverse.extend(a)

# 3-й способ
# for el in range((len(my_list) // 2) + 1):
#     el1 = el * 2
#     a = my_list[el1:el1+2][::-1]
#     my_list_reverse.extend(a)

print(f"Соседние элементы списка поменялись местами: {my_list_reverse}")
