from collections import deque
from functools import reduce

NUMBER_OF_ROUNDS = 10000


class Monkey:
    def __init__(self, id_number, items, operation, test, true_target, false_target):
        self.id_number = id_number
        self.items = items
        self.operation = operation
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspected_items = 0

    def InspectItem(self, item):
        if "+" in self.operation[0]:
            return (item + int(self.operation[-1])) # // 3
        elif ("*" in self.operation[0]) and ("old" not in self.operation[-1]):
            return (item * int(self.operation[-1])) # // 3
        else:
            return (item**2) # // 3

    def TestWorry(self, worry_level):
        return self.true_target if worry_level % self.test == 0 else self.false_target

    def PassItem(self):
        self.items.popleft()

    def ReceiveItem(self, item):
        self.items.append(item)

    def AddToInspected(self):
        self.inspected_items += 1


if __name__ == "__main__":
    with open("monkey_properties.txt") as f:
        lines = f.readlines()

    monkey_descriptions = "".join(lines).split("\n\n")

    monkey_dict = {}
    for monkey_description in monkey_descriptions:
        monkey_description_lines = monkey_description.split("\n")
        monkey_id = monkey_description_lines[0].split(" ")[-1].rstrip(":")
        items = deque(
            [
                int(item.strip())
                for item in monkey_description_lines[1].split(":")[-1].split(",")
            ]
        )
        operation = monkey_description_lines[2].split("old ")[-1].split(" ")
        test = int(monkey_description_lines[3].split(" ")[-1])
        true_target = monkey_description_lines[4].split(" ")[-1]
        false_target = monkey_description_lines[5].split(" ")[-1]
        monkey_dict[monkey_id] = Monkey(monkey_id, items, operation, test, true_target, false_target)

    tests = [monkey.test for monkey in monkey_dict.values()]
    reducer = reduce((lambda x, y: x * y), tests)

    for i in range(NUMBER_OF_ROUNDS):
        for monkey in monkey_dict.values():
            for item in list(monkey.items):
                worry_level = monkey.InspectItem(item)
                if worry_level > reducer:
                    k = worry_level // reducer
                    worry_level = worry_level - (k*reducer)
                target = monkey.TestWorry(worry_level)
                monkey.PassItem()
                monkey_dict[target].ReceiveItem(worry_level)
                monkey.AddToInspected()

    for monkey_id, monkey in monkey_dict.items():
        print(f"Monkey {monkey_id} inspected {monkey.inspected_items} items")

    activity_list = sorted([activity for activity in [monkey.inspected_items for monkey in monkey_dict.values()]])
    monkey_business = activity_list[-2] * activity_list[-1]
    print(f"Total monkey business is {monkey_business}")
