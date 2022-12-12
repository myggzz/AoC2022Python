input = open("Input.txt", "r").read().splitlines()

cycle_count = 0
x = 1
signal_str = []
crt_x = 0


def parse_input(input):
    if input != "noop":
        return int(input.split(" ")[1])
    else:
        return 0

def addx(value, cycle_count, x, crt_x):
    for _ in range(2):
        cycle_count += 1
        crt_x += 1
        if cycle_count % 20 == 0:
            signal_str.append(x * cycle_count)
    x += value
    return cycle_count, x, crt_x


def noop(cycle_count, x, crt_x):
    cycle_count += 1
    crt_x += 1
    if cycle_count % 20 == 0:
        signal_str.append(x * cycle_count)
    return cycle_count, crt_x

for line in input:
    value = parse_input(line)
    if value != 0:
        cycle_count, x, crt_x = addx(value, cycle_count, x, crt_x)
    else:
        cycle_count, crt_x = noop(cycle_count, x, crt_x)
print(sum(signal_str[0::2]))
