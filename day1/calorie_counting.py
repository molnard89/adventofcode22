def total_calories(calorie_list):
    kcal_totals = []
    for elf in calorie_list:
        kcal_values = [int(kcal) for kcal in elf[1:-1].split(",")]
        kcal_totals.append(sum(kcal_values))
    return kcal_totals


with open("calorie_per_elf_list.txt") as f:
    lines = f.readlines()

kcal_list = []
for line in lines:
    separator = "" if len(line) > 1 else ";"
    kcal_list.append(line.replace("\n", separator))

kcal_list = ",".join(kcal_list).split(";")
kcal_totals = total_calories(kcal_list)

highest_kcal_list = []
n = 3
for i in range(n):
    max_kcal = max(kcal_totals)
    highest_kcal_list.append(max_kcal)
    print(f"{i+1}. highest calories carried by a single elf = {max_kcal}")
    kcal_totals.remove(max_kcal)

print(f"Total calories carried by the top {n} elves = {sum(highest_kcal_list)}")
