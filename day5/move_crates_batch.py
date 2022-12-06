from move_crates import parse_initial_setup

if __name__ == "__main__":
    stacks = parse_initial_setup()

    with open('container_movement_plan.txt') as f:
        command_strings = f.readlines()[10:]

    for command in command_strings:
        number_of_crates, from_stack, to_stack = ([int(x) for x in command.strip().split(' ') if x.isdigit()])
        from_stack, to_stack = from_stack-1, to_stack-1
        number_of_crates = -1 * number_of_crates
        crates_being_moved = list(stacks[from_stack])[number_of_crates:]
        for crate in crates_being_moved:
            stacks[to_stack].append(crate)
            stacks[from_stack].pop()

    print("Top crate in all stacks after moving:")
    for stack in stacks:
        print(stack[-1], end="")
