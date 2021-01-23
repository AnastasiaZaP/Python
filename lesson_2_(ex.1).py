my_list = [12, "hello"]
print(my_list)
my_list.append(True)
my_list.append(17.49)
my_list.insert(0, "apple")
my_list.insert(3, None)
my_list.append((5, 6, 7))
my_list.insert(2, {1: "book", 2: 5.799})
print(my_list)
for el in my_list:
    print(type(el))


