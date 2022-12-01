with open("calorie_per_elf_list.txt") as f:
    lines = f.readlines()

kcal_list = []
for line in lines:
    separator = "" if len(line) > 1 else ";"
    kcal_list.append(line.replace("\n", separator))

kcal_list = ",".join(kcal_list).split(";")

kcal_totals = []
for elf in kcal_list:
    kcal_values = [int(kcal) for kcal in elf[1:-1].split(",")]
    kcal_totals.append(sum(kcal_values))

print(f"Most calories in total carried by a single elf: {max(kcal_totals)}")
