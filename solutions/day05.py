from collections import defaultdict
import copy


with open("../inputs/day05.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


seeds = [int(seed) for seed in lines[0].split("seeds: ")[1].split(" ")]
lines = [line for line in lines[2:] if line]

maps = defaultdict(list)
current_map = None
for line in lines:
    if "map:" in line:
        current_map = line.split(" map:")[0]
        continue

    numbers = [int(n) for n in line.split(" ")]
    maps[current_map].append(
        {
            "destination": int(numbers[0]),
            "source": int(numbers[1]),
            "range": int(numbers[2]),
        }
    )

# Part 1


def seed_new_place(seed: int, map: list[dict]) -> int:
    for mapping in map:
        # print(mapping)
        if seed >= mapping["source"] and seed < mapping["source"] + mapping["range"]:
            diff = seed - mapping["source"]
            #   print(diff)
            return mapping["destination"] + diff

    return seed


mapped_seeds = copy.copy(seeds)
for name, mappings in maps.items():
    for i, seed in enumerate(mapped_seeds):
        mapped_seeds[i] = seed_new_place(seed, mappings)


# print(min(mapped_seeds))

# Part 2

extended_mapped_seeds = []
for i in range(0, len(seeds), 2):
    extended_mapped_seeds.extend([seeds[i] + x for x in range(seeds[i + 1])])

# 💀
print(len(extended_mapped_seeds))
for name, mappings in maps.items():
    for i, seed in enumerate(extended_mapped_seeds):
        extended_mapped_seeds[i] = seed_new_place(seed, mappings)

print(min(extended_mapped_seeds))
