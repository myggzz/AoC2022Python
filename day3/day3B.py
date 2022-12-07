with open('input.txt') as f:
    sum_of_prio = 0
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    i = 0
    while i < len(lines):
        for char in lines[i]:
            if char in lines[i+1] and char in lines[i+2]:
                if char.islower():
                    sum_of_prio =  sum_of_prio + ord(char) - 96
                else:
                    sum_of_prio = sum_of_prio + ord(char) - 38
                i = i + 3
                break
    print(sum_of_prio) 