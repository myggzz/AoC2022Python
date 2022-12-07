score_sheet = {
    "A" : {
        "Y": 4,
        "X": 3,
        "Z": 8},
    "B" : {
        "Y": 5,
        "X": 1,
        "Z": 9
    }, 
    "C" : {
        "Y": 6,
        "X": 2, 
        "Z": 7
    }
}
total_score = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        total_score = total_score + score_sheet[line[0]][line[2]]
print(total_score)