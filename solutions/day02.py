with open("../inputs/day02.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


# Part 1


def is_game_possible(game_draws: list[str]) -> bool:
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for set in sets:
        for draw in set.split(", "):
            number, color = draw.split(" ")
            if int(number) > constraints[color]:
                return False

    return True


possible_ids = []
for line in lines:
    game_info, raw_sets = line.split(": ")
    game_id = int(game_info.split(" ")[1])
    sets = raw_sets.split("; ")

    print(line, game_id)
    if is_game_possible(sets):
        possible_ids.append(game_id)


print(sum(possible_ids))

# Part 2


def game_power(game_draws: list[str]) -> int:
    min_draws = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set in sets:
        for draw in set.split(", "):
            number, color = draw.split(" ")
            if int(number) > min_draws[color]:
                min_draws[color] = int(number)

    return min_draws["red"] * min_draws["green"] * min_draws["blue"]


total_power = 0
for line in lines:
    game_info, raw_sets = line.split(": ")
    game_id = int(game_info.split(" ")[1])
    sets = raw_sets.split("; ")

    total_power += game_power(sets)


print(total_power)
