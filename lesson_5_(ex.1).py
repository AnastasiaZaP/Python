with open("grocery_list.txt", "w", encoding="utf-8") as my:
    while True:
        a = input("Собираетесь в магазин? Напишите список покупок: ")
        my.write(f"{a}\n")
        if a == "":
            break
