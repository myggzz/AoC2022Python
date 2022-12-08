file_name = "input.txt"
text_file = open(file_name)

data = text_file.read().split('\n')

def check_overlap(a, b, x, y):
    if a < x and b < x:
        return False
    if a > y and b > y:
        return False
    return True

score = 0
for row in data:
    first_elf_section, second_elf_section = row.split(',')

    first_elf_first_number, first_elf_second_number = list(map(int, first_elf_section.split('-')))
    second_elf_first_number, second_elf_second_number = list(map(int, second_elf_section.split('-')))

    if check_overlap(first_elf_first_number, first_elf_second_number, second_elf_first_number, second_elf_second_number):
        score += 1
        print(row)

print(score)
