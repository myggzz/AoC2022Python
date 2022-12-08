with open("input.txt") as f:
    input = f.read()
    for i in range(len(input)):
        check_set = set()
        for x in range(14):
            check_set.add(input[i+x])
        if len(check_set) == 14:
            print(i+14)
            break