import numpy as np


def find_letter_in_grid(grid, char_to_find):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == char_to_find:
                return i, j


def convert_sa(char):
    if char == "S":
        char = chr(ord("a") - 1)
    elif char == "E":
        char = chr(ord("z") + 1)
    return char


def check_adjacency(char1, char2):
    char1, char2 = convert_sa(char1), convert_sa(char2)
    return ord(char2) - ord(char1) < 2


def step_through(map_grid, N):
    line_length, row_length = len(map_grid), len(map_grid[0].strip())
    distance_grid = np.zeros([line_length, row_length])
    start_line, start_row = find_letter_in_grid(map_grid, "S")
    distance_grid[start_line][start_row] = 1

    for k in range(1, N+1):
        for i in range(line_length):
            for j in range(row_length):
                if distance_grid[i][j] == k:
                    current_elevation = lines[i][j]
                    if current_elevation == "E":
                        print(f"Found the end point, its distance is {k-1}")
                        return distance_grid
                    if (i > 0) and (distance_grid[i-1][j]) == 0 and (check_adjacency(current_elevation, lines[i-1][j])):
                        distance_grid[i-1][j] = k+1
                    if (j > 0) and (distance_grid[i][j-1]) == 0 and (check_adjacency(current_elevation, lines[i][j-1])):
                        distance_grid[i][j-1] = k+1
                    if (i < (line_length-1)) and (distance_grid[i+1][j]) == 0 and (check_adjacency(current_elevation, lines[i+1][j])):
                        distance_grid[i+1][j] = k+1
                    if (j < (row_length-1)) and (distance_grid[i][j+1]) == 0 and (check_adjacency(current_elevation, lines[i][j+1])):
                        distance_grid[i][j+1] = k+1
    return distance_grid


if __name__ == "__main__":
    with open("map.txt") as f:
        lines = f.readlines()

    steps = 1000
    dist_grid = np.array(step_through(lines, steps))
