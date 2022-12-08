with open("input.txt") as f:
    input = f.read()
    for i in range(len(input)):
        set = {input[i], input[i+1], input[i+2], input[i+3]}
        print(set)
        if len(set) == 4:
            print(i+4)
            break