score_sheet = {
    "A" : {
        "Y": 8,
        "X": 4,
        "Z": 3},
    "B" : {
        "Y": 5,
        "X": 1,
        "Z": 9
    }, 
    "C" : {
        "Y": 2,
        "X": 7, 
        "Z": 6
    }
}

total_score = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        total_score = total_score + score_sheet[line[0]][line[2]]

print(total_score)