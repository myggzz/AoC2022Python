input = open("input.txt", "r").read().splitlines()

cycle_count = 0
x = 1
signal_str = []
crt_x = 0


def parse_input(input):
    if input != "noop":
        return int(input.split(" ")[1])
    else:
        return 0


def check_sync(crt_x, x):
    if crt_x == x or crt_x == x + 1 or crt_x == x - 1:
        return True
    return False


def write_pixel(crt_x):
    if crt_x < 39:
        print("#", end="")
    else:
        print("#\n", end="")


def write_dot(crt_x):
    if crt_x < 39:
        print(".", end="")
    else:
        print(".\n", end="")


def addx(value, cycle_count, x, crt_x):
    for _ in range(2):
        synced = check_sync(crt_x, x)
        if synced:
            write_pixel(crt_x)
        else:
            write_dot(crt_x)
        cycle_count += 1
        crt_x += 1
        if cycle_count % 40 == 0:
            crt_x = 0
    x += value
    return cycle_count, x, crt_x


def noop(cycle_count, x, crt_x):
    synced = check_sync(crt_x, x)
    if synced:
        write_pixel(crt_x)
    else:
        write_dot(crt_x)
    cycle_count += 1
    crt_x += 1
    if cycle_count % 40 == 0:
        crt_x = 0
    return cycle_count, crt_x


for line in input:
    value = parse_input(line)
    if value != 0:
        cycle_count, x, crt_x = addx(value, cycle_count, x, crt_x)
    else:
        cycle_count, crt_x = noop(cycle_count, x, crt_x)
