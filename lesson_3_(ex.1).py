def div(delimoe, delitel):
    chastnoe = delimoe / delitel
    return chastnoe

a = int(input("Введите делимое = "))
while True:
    b = int(input("Введите делитель = "))
    if b == 0:
        print("Делитель не должен равняться нулю!")
    else:
        print(f"Частное = {div(a, b)}")
        break