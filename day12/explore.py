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


def step_through(map_grid, starting_points, N):
    line_length, row_length = len(map_grid), len(map_grid[0].strip())
    distance_grid = np.zeros([line_length, row_length])
    start_line, start_row = starting_points
    distance_grid[start_line][start_row] = 1

    for k in range(1, N+1):
        for i in range(line_length):
            for j in range(row_length):
                if distance_grid[i][j] == k:
                    current_elevation = map_grid[i][j]
                    if current_elevation == "E":
                        return k-1
                    if (i > 0) and (distance_grid[i-1][j]) == 0 and (check_adjacency(current_elevation, map_grid[i-1][j])):
                        distance_grid[i-1][j] = k+1
                    if (j > 0) and (distance_grid[i][j-1]) == 0 and (check_adjacency(current_elevation, map_grid[i][j-1])):
                        distance_grid[i][j-1] = k+1
                    if (i < (line_length-1)) and (distance_grid[i+1][j]) == 0 and (check_adjacency(current_elevation, map_grid[i+1][j])):
                        distance_grid[i+1][j] = k+1
                    if (j < (row_length-1)) and (distance_grid[i][j+1]) == 0 and (check_adjacency(current_elevation, map_grid[i][j+1])):
                        distance_grid[i][j+1] = k+1
    return k-1


def find_all_occurances(str_grid, elevation):
    coordinates = []
    for i, line in enumerate(str_grid):
        for j, char in enumerate(line):
            if char == elevation:
                coordinates.append((i, j))
    return coordinates


if __name__ == "__main__":
    with open("map.txt") as f:
        elevation_map = f.readlines()

    a_levels = find_all_occurances(elevation_map, "a")
    print(f"Number of positions with 'a' level = {len(a_levels)}")

    steps = 1000
    distance = step_through(elevation_map, find_letter_in_grid(elevation_map, "S"), steps)
    print(f"Distance required to reach 'E' is {distance}")

    shortest_distance = distance
    print("Computing closest 'a' level to 'E'...")
    for i, starting_coordinate in enumerate(a_levels):
        distance = step_through(elevation_map, starting_coordinate, shortest_distance+1)
        shortest_distance = min([distance, shortest_distance])
        if i % 10 == 0:
            print(f"{i/len(a_levels)*100} % done")

    print(f"Closest 'a' elevation point to 'E' is {shortest_distance}")
