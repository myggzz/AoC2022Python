file_name = "input.txt"
with open(file_name, 'r') as f:
    data = f.read().split('\n')

x = 1
cycle = 0
sprite = []

def check_and_add(cycle, x):
    if (x-1) <= cycle % 40 <= (x+1):
        sprite.append("#")
    else:
        sprite.append(".")
    return

for line in data:
    if line.startswith("noop"):
        check_and_add(cycle, x)
        cycle += 1
    else:
        for i in range(0,2):
            check_and_add(cycle, x)
            cycle += 1
        x += int(line.split(' ')[1])

for i, pixel in enumerate(sprite):
    if i % 40 == 0:
        print('\n')
    if pixel == ".":
        print("░░", end='')
    else:
        print("██", end='')

print('\n\n')