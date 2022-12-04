import string
priorities = {
    letter: index for index, letter in enumerate(string.ascii_letters, start=1)
}


if __name__ == "__main__":
    with open("rucksack_content.txt") as f:
        rucksack_content = f.readlines()
    rucksack_content = [line.strip() for line in rucksack_content]

    total_priorities = 0
    for rucksack in rucksack_content:
        compartment_size = int(len(rucksack)/2)
        compartment1 = rucksack[:compartment_size]
        compartment2 = rucksack[compartment_size:]
        common = list(set.intersection(*map(set, [compartment1, compartment2])))
        total_priorities += priorities[common[0]]

    print(f"Total priorities in all rucksacks = {total_priorities}")
