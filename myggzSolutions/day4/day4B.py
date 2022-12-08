with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    count_pairs = 0
    for line in lines:
        first_elf_sections , second_elf_sections = line.split(",")
        f1, f2 = list(map(int, first_elf_sections.split("-")))
        s1, s2 = list(map(int, second_elf_sections.split("-")))
        for item in range(f1, f2 + 1):
            if item in range(s1, s2 + 1):
                count_pairs += 1
                break
    print(count_pairs)