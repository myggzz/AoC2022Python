with open('input.txt') as f:
    lines = f.readlines()
    all_elves_calories = []
    elve_calories = 0
    for line in lines:
        if line == '\n':
            all_elves_calories.append(elve_calories)
            elve_calories = 0
        else:
            elve_calories = elve_calories + int(line)

all_elves_calories.sort(reverse=True)
top3_total = 0
for i in range(3):
    top3_total = top3_total + all_elves_calories[i]
print(top3_total)