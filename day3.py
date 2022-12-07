file_name = "input.txt"
text_file = open(file_name)
data = text_file.read().split('\n')

def get_score_of_character(c):
    if c.isupper():
        return ord(c) - 38
    return ord(c) - 96

score = 0
for count, items in enumerate(data):
    if count % 3 == 0:
        for item in items:
            if item in data[count + 1] and item in data[count + 2]:
                score += get_score_of_character(item)
                break
print(score)