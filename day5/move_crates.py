from collections import deque
import itertools


def strip_zeros(input_list):
    return [elem for elem in input_list if elem != '0']


def parse_initial_setup():
    with open("container_movement_plan.txt", "r") as f:
        container_input = [next(f) for x in range(8)]
    container_initial_setup = [line[1::4] for line in container_input]
    container_initial_config = [[char for char in line] for line in container_initial_setup]
    transposed_array = itertools.zip_longest(*container_initial_config)
    return [deque([char for char in elem[-1::-1] if char != ' ']) for elem in transposed_array]


if __name__ == "__main__":
    stacks = parse_initial_setup()

    with open('container_movement_plan.txt') as f:
        command_strings = f.readlines()[10:]

    for command in command_strings:
        number_of_crates, from_stack, to_stack = ([int(x) for x in command.strip().split(' ') if x.isdigit()])
        from_stack, to_stack = from_stack-1, to_stack-1
        for _ in range(number_of_crates):
            crate_being_moved = stacks[from_stack][-1]
            stacks[from_stack].pop()
            stacks[to_stack].append(crate_being_moved)

    print("Top crate in all stacks after moving:")
    for stack in stacks:
        print(stack[-1], end="")