file_name = "input.txt"
with open(file_name, 'r') as f:
    data = f.read().split('\n')

x = 1
cycle = 1
signal_strengths = []

def check_and_add():
    if cycle in (20, 60, 100, 140, 180, 220):
        signal_strengths.append(cycle * x)
    return

for line in data:
    if line.startswith("noop"):
        check_and_add()
        cycle += 1
    else:
        for i in range(0,2):
            check_and_add()
            cycle += 1
        x += int(line.split(' ')[1])

print(sum(signal_strengths))