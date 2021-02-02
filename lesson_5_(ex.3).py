with open("text_3.txt", "r", encoding="utf-8") as my:
    inp_list = my.readlines()
    list_to_dict = dict((inp_list[i].split()[0],float(inp_list[i].split()[1])) for i in range(len(inp_list)))
    print(f"Сотрудники, чей оклад составляет < оклад менее 20000:")
    for key in list_to_dict:
        if list_to_dict.get(key) < 20000:
            print(f"{key}")
    average_fee = sum(list_to_dict.values())/len(list_to_dict)
    print(f"\nСредняя величина дохода сотрудников составляет:\n{average_fee}")
