from pathlib import Path

if __name__ == "__main__":
    cwd = Path("/")
    #with open("terminal_output.txt") as f:
    with open("example_input.txt") as f:
        terminal = f.readlines()[1:]
    dir_size_dict = {}
    for i, line in enumerate(terminal):
        line = line.strip()
        #if i == 21:
        #    break
        if line.startswith("$") and line[2:4] == "cd":
            move_to = line[5:]
            cwd = cwd / move_to if ".." not in move_to else cwd.parent
        elif line[0].isdigit():
            file_size = int(line.split(" ")[0])
            dir_size_dict[cwd.as_posix()] = (
                file_size
                if cwd.as_posix() not in dir_size_dict.keys()
                else dir_size_dict[cwd.as_posix()] + file_size
            )

    print(len(dir_size_dict.keys()))

    #print(dir_size_dict)
    #print("*"*50)

    reference_dict = dir_size_dict.copy()
    # add the size of subfolders to parents
    for folder in reference_dict.keys():
        for other_folder, size_in_other_folder in reference_dict.items():
            if (folder != other_folder) and (Path(folder) in [fold for fold in Path(other_folder).parents]):
                dir_size_dict[folder] = dir_size_dict[folder] + size_in_other_folder

    print(dir_size_dict)

    small_directories = dict((k, v) for k, v in dir_size_dict.items() if v <= 100000)

    print(len(small_directories.keys()))

    # filter out nested folders
    #reference_dict = small_directories.copy()
    #for folder in reference_dict.keys():
    #    for other_folder in reference_dict.keys():
    #        if (folder != other_folder) and (Path(folder) in [fold for fold in Path(other_folder).parents]):
    #            small_directories.pop(other_folder)
    #            print(folder)
    #            print(other_folder)
    #            print("*"*50)

    for kv in small_directories.items():
        print(kv)
    sum_sizes = sum(small_directories.values())
    print(f"Total size of small directories = {sum_sizes}")
