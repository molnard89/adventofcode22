from rucksack_check import priorities


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


with open("rucksack_content.txt") as f:
    rucksack_content = f.readlines()
rucksack_content = [line.strip() for line in rucksack_content]

total_priorities = 0
for group in chunker(rucksack_content, 3):
   common = list(set(group[0]).intersection(group[1], group[2]))[0]
   total_priorities += priorities[common]

print(f"Total priorities of badges in all groups = {total_priorities}")
