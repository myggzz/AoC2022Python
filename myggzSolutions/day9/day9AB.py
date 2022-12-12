input = open("input.txt", "r").read().splitlines()

knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
part1 = set()
part2 = set()


def parse_input(input):
    direction = input[0]
    steps = int(input.split(" ")[1])
    return direction, steps


def not_adjacent(prev_knot, curr_knot):
    xdiff = abs(prev_knot[0] - curr_knot[0])
    ydiff = abs(prev_knot[1] - curr_knot[1])

    if xdiff <= 1 and ydiff <= 1:
        return False
    return True


def new_position(prev_knot, curr_knot):
    offsetx = find_direction(prev_knot[0] - curr_knot[0])
    offsety = find_direction(prev_knot[1] - curr_knot[1])
    newx = curr_knot[0] + offsetx
    newy = curr_knot[1] + offsety
    return [newx, newy]


def find_direction(value):
    if value == 0:
        return 0
    elif value > 0:
        return 1
    else:
        return -1


for line in input:
    direction, steps = parse_input(line)
    for step in range(steps):
        if direction == "D":
            knots[0][1] -= 1
        elif direction == "U":
            knots[0][1] += 1
        elif direction == "R":
            knots[0][0] += 1
        else:
            knots[0][0] -= 1
        for prev_knot, curr_knot in enumerate(range(1, len(knots))):
            if not_adjacent(knots[prev_knot], knots[curr_knot]):
                knots[curr_knot] = new_position(knots[prev_knot], knots[curr_knot])
        part1.add(tuple(knots[1]))
        part2.add(tuple(knots[9]))
print(f"Part 1 : {len(part1)}")
print(f"Part 2 : {len(part2)}")
