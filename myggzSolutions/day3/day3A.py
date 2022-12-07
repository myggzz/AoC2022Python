with open("input.txt") as f:
    sum_of_prio = 0
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        length = len(line)
        mid_slice = int(length/2)
        first_half = line[:(mid_slice)]
        second_half = line[mid_slice:length]
        for char in first_half:
            if char in second_half:
                if char.islower():
                    sum_of_prio =  sum_of_prio + ord(char) - 96
                else:
                    sum_of_prio = sum_of_prio + ord(char) - 38
                break
    print(sum_of_prio)