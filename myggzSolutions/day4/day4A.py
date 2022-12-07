with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    count_pairs = 0
    for line in lines:
        first_elf_sections , second_elf_sections = line.split(",")
        f1, f2 = list(map(int, first_elf_sections.split("-")))
        s1, s2 = list(map(int, second_elf_sections.split("-")))
        if (s1 >= f1 and s2 <= f2) or (f1 >= s1 and f2 <= s2):
            count_pairs = count_pairs + 1
    print(count_pairs)