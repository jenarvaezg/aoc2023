with open("input01.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


# total = 0
# for line in lines:
#     digit = 0
#     for c in line:
#         if c.isdigit():
#             digit += 10 * int(c)
#             break
#     for c in reversed(line):
#         if c.isdigit():
#             digit += int(c)
#             break

#     total += digit

# print(total)


def get_first_number(line) -> int:
    for offset in range(len(line)):
        effective_line = line[:offset]

        for i, number_str in enumerate(number_strs):
            if number_str in effective_line:
                return i + 1

        if line[offset].isdigit():
            return int(line[offset])
    raise Exception


def get_last_number(line) -> int:
    for offset in range(len(line)):
        effective_line = line[len(line) - offset - 1 : len(line)]
        for i, number_str in enumerate(number_strs):
            if number_str in effective_line:
                return i + 1

        if effective_line[len(effective_line) - offset - 1].isdigit():
            return int(effective_line[len(effective_line) - offset - 1])
    raise Exception


number_strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total2 = 0
for line in lines:
    digit = get_first_number(line) * 10 + get_last_number(line)

    total2 += digit

print(total2)
