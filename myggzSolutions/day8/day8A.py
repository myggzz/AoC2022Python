input = open("input.txt", "r").read().splitlines()


def count_edge_trees(input):
    edge_tree_count = ((len(input[0]) * 2) + (len(input) * 2)) - 4
    return edge_tree_count


def check_inside_trees(height, width, input, total_visible):
    # For every treerow except first and last row
    for row in range(1, height - 1):
        # For every column in that row except first and last column
        for column in range(1, width - 1):
            # print(row, column, input[row][column])
            tree_visibility = {"up": True, "down": True, "left": True, "right": True}
            for above_rows in range(row):
                if input[row][column] <= input[above_rows][column]:
                    tree_visibility["up"] = False
                    break
            # check down
            for below_rows in range(row + 1, height):
                if input[row][column] <= input[below_rows][column]:
                    tree_visibility["down"] = False
                    break
            # check left
            for left_columns in range(column):
                if input[row][column] <= input[row][left_columns]:
                    tree_visibility["left"] = False
                    break
            # check right
            for right_columns in range(column + 1, width):
                if input[row][column] <= input[row][right_columns]:
                    tree_visibility["right"] = False
                    break
            for value in tree_visibility.values():
                if value == True:
                    total_visible += 1
                    break
    return total_visible


height = int(len(input))
width = int(len(input[0]))
total_visible = count_edge_trees(input)
total_visible = check_inside_trees(height, width, input, total_visible)
print(total_visible)
