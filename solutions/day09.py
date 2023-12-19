import copy


with open("../inputs/day09.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

all_histories = []
for line in lines:
    numbers = [int(x) for x in line.split(" ")]
    line_histories = [copy.copy(numbers)]
    current_history = line_histories[0]
    while not all(x == 0 for x in current_history):
        next_history = [
            current_history[i + 1] - current_history[i]
            for i in range(len(current_history) - 1)
        ]
        line_histories.append(next_history)
        current_history = next_history
    all_histories.append(line_histories)

# Part 1
result_numbers = []
for histories in all_histories:
    result_numbers.append(sum(history[-1] for history in histories))

print(sum(result_numbers))

# Part 2
result_numbers = []
for histories in all_histories:
    bottom = 0
    for history in reversed(histories[:-1]):
        # bottom = right - left
        # left = right - bottom
        right = history[0]
        bottom = right - bottom
    result_numbers.append(bottom)

print(sum(result_numbers))
