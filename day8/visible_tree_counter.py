def check_visibility_in_line(line_of_trees, reference_tree_location):
    reference_tree = line_of_trees[reference_tree_location]
    visibility_left = all(
        [tree < reference_tree for tree in line_of_trees[:reference_tree_location]]
    )
    visibility_right = all(
        [tree < reference_tree for tree in line_of_trees[reference_tree_location+1:]]
    )
    return any([visibility_left, visibility_right])


def make_column_cross_section(tree_rows, column_index):
    return "".join([row[column_index] for row in tree_rows])


if __name__ == "__main__":
    with open("tree_map.txt") as f:
        tree_map = f.readlines()
    tree_map = [row.strip() for row in tree_map]

    visible_trees = 0
    for row_index, row in enumerate(tree_map):
        for tree_index in range(len(row)):
            if check_visibility_in_line(row, tree_index):
                visible_trees += 1
                continue
            column = make_column_cross_section(tree_map, tree_index)
            if check_visibility_in_line(column, row_index):
                visible_trees += 1
                continue

    print(f"Number of visible trees = {visible_trees}")
