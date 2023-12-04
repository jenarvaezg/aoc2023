import math


with open("../inputs/day04.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


def clean_numbers(raw: str) -> list[int]:
    return [int(n.strip()) for n in raw.strip().split(" ") if n]


cards = []
for line in lines:
    _, numbers = line.split(": ")
    raw_winning_numbers, raw_card_numbers = numbers.split("|")

    cards.append(
        (
            clean_numbers(raw_winning_numbers),
            clean_numbers(raw_card_numbers),
        )
    )


# Part 1
def card_match_count(card: tuple[list[int], list[int]]) -> int:
    match_count = 0
    for number in card[1]:
        if number in card[0]:
            match_count += 1

    return match_count


def card_points(card: tuple[list[int], list[int]]) -> int:
    if not (match_count := card_match_count(card)):
        return 0

    return int(math.pow(2, match_count - 1))


print(sum(card_points(card) for card in cards))

# Part 2


card_counts = [1 for _ in cards]
for i, card in enumerate(cards):
    match_count = card_match_count(card)
    for j in range(i + 1, i + 1 + match_count):
        card_counts[j] += card_counts[i]

print(sum(card_counts))
