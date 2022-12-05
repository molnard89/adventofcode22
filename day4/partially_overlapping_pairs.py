def list_contains_some(list1, list2):
    return 1 if any(x in list1 for x in list2) else 0


overlapping_schedules = 0
with open("cleaning_schedule.txt") as f:
    for line in f.readlines():
        schedule = line.strip().split(",")
        elf1, elf2 = schedule[0].split("-"), schedule[1].split("-")
        elf1_schedule = [i for i in range(int(elf1[0]), int(elf1[1])+1)]
        elf2_schedule = [i for i in range(int(elf2[0]), int(elf2[1])+1)]
        contains1 = list_contains_some(elf1_schedule, elf2_schedule)
        contains2 = list_contains_some(elf2_schedule, elf1_schedule)
        overlapping_schedules += max(contains1, contains2)

print(f"Number of partially overlapping schedules = {overlapping_schedules}")
