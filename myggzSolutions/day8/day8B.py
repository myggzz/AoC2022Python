input = open("input.txt", "r").read().splitlines()

# Fuck this solution
def check_inside_trees(height, width, input):
    best_visibility_score = 0
    # For every treerow except first and last row
    for row in range(1, height - 1):
        # For every column in that row except first and last column
        for column in range(1, width - 1):
            tree_visibility = {"up": 0, "down": 0, "left": 0, "right": 0}
            # check up
            for above_rows in range(row):
                if input[row][column] <= input[row - above_rows - 1][column]:
                    tree_visibility["up"] += 1
                    break
                tree_visibility["up"] += 1
            # check down
            for below_rows in range(row + 1, height):
                if input[row][column] <= input[below_rows][column]:
                    tree_visibility["down"] += 1
                    break
                tree_visibility["down"] += 1
            # check left
            for left_columns in range(column):
                if input[row][column] <= input[row][column - left_columns - 1]:
                    tree_visibility["left"] += 1
                    break
                tree_visibility["left"] += 1
            # check right
            for right_columns in range(column + 1, width):
                if input[row][column] <= input[row][right_columns]:
                    tree_visibility["right"] += 1
                    break
                tree_visibility["right"] += 1
            visibility_score = (
                tree_visibility["up"]
                * tree_visibility["down"]
                * tree_visibility["left"]
                * tree_visibility["right"]
            )
            if visibility_score > best_visibility_score:
                best_visibility_score = visibility_score
    return best_visibility_score


height = int(len(input))
width = int(len(input[0]))
best_visibility_score = check_inside_trees(height, width, input)
print(best_visibility_score)
