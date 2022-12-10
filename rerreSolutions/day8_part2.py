file_name = "input.txt"
text_file = open(file_name)

data = text_file.read().split('\n')
rows = len(data)
len_row = len(data[0])

def check_surrounding(close_trees, tree):
    visible_trees = 0
    for close_tree in list(map(int, close_trees)):
        if close_tree < int(tree):
            visible_trees += 1
        else:
            visible_trees += 1
            break
    return visible_trees

highest = 0
for count_row, row in enumerate(data):
    for count_tree, tree in enumerate(row):

        trees_right = list(row[count_tree+1:])
        trees_left = list(row[:count_tree])
        trees_left.reverse()
        trees_up = [y_row[count_tree] for y_row in data[:count_row]]
        trees_up.reverse()
        trees_down = [y_row[count_tree] for y_row in data[count_row+1:]]

        surrounding_trees = [trees_right, trees_left, trees_up, trees_down]

        #print(tree)
        #print(trees_left)
        #print(trees_right)
        #print(trees_up)
        #print(trees_down)

        this_visible_trees = 1
        for trees in surrounding_trees:
            this_visible_trees *= check_surrounding(trees, tree)

        if this_visible_trees > highest:
            highest = this_visible_trees

print(highest)