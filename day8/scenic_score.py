from visible_tree_counter import make_column_cross_section


def find_blocking_tree(line_of_trees, reference_tree_location, direction):
    reference_tree = line_of_trees[reference_tree_location]
    line_of_tree_slice = (
        line_of_trees[reference_tree_location + 1 :]
        if direction == "r"
        else line_of_trees[:reference_tree_location][::-1]
    )
    distance = 0
    for tree in line_of_tree_slice:
        distance += 1
        if reference_tree <= tree:
            break
    return distance


if __name__ == "__main__":
    test_trees = ["30373", "25512", "65332", "33549", "35390"]

    with open("tree_map.txt") as f:
        tree_map = f.readlines()
    tree_map = [row.strip() for row in tree_map]

    scenic_scores = []

    for row_index, row in enumerate(tree_map):
        for tree_index in range(len(row)):
            column = make_column_cross_section(tree_map, tree_index)
            scenic_score = 1
            for direction in ["r", "l"]:
                scenic_score *= find_blocking_tree(row, tree_index, direction)
                scenic_score *= find_blocking_tree(column, row_index, direction)
            scenic_scores.append(scenic_score)

    print(f"Maximal scenic score = {max(scenic_scores)}")
