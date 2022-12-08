file_name = "input.txt"
text_file = open(file_name)
data = list(text_file.read())

for counter, character in enumerate(data):
    if counter + 14 < len(data):
        four_char = data[counter:counter+14]
        if len(set(four_char)) == 14:
            print("Found it at " + str(counter + 14))
