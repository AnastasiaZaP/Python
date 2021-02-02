with open("text_3.txt", "r", encoding="utf-8") as my:
    a = my.readlines()
    print(f"Количество строк в исходном файле = {len(a)}")
    for el in range(len(a)):
        print(f"В строке № {el + 1} количество слов = {len(a[el].split())}")