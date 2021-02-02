import json
with open("text_7.txt", "r", encoding="utf-8") as inp_file:
    inp_list = inp_file.readlines()
    print(inp_list)
profit = [int(inp_list[index].split()[2]) - int(inp_list[index].split()[3]) for index in range(len(inp_list))]
print(f"Прибыль каждой компании соответственно: {profit}")
average_profit = 0
count = 0
for el in profit:
    if el >= 0:
        average_profit += el
        count += 1
if count != 0:
    average_profit /= count
print(f"Средняя прибыль = {average_profit}")
out_list = [{inp_list[index].split()[0]: profit[index] for index in range(len(inp_list))},
            {"average_profit": average_profit}]
print(out_list)
with open("7_json.json", "w", encoding="utf-8") as out_file:
    json.dump(out_list, out_file, ensure_ascii=False, indent=4)
