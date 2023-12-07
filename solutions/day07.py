from dataclasses import dataclass
from functools import cached_property, cmp_to_key

with open("../inputs/day07.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


@dataclass
class Hand:
    cards: list[str]
    bid: int
    part: int

    @cached_property
    def unique_cards(self) -> set[str]:
        return set(self.cards)

    @cached_property
    def card_counts(self) -> list[int]:
        return [len([x for x in self.cards if x == c]) for c in self.unique_cards]

    @cached_property
    def card_counts_not_joker(self) -> list[int]:
        return [
            len([x for x in self.cards if x == c and c != "J"])
            for c in self.unique_cards
        ]

    @cached_property
    def joker_count(self) -> int:
        return len([x for x in self.cards if x == "J"])

    def card_value(self, card: str) -> int:
        match card:
            case "A":
                return 14
            case "K":
                return 13
            case "Q":
                return 12
            case "J":
                return 11 if self.part == 1 else 1
            case "T":
                return 10
            case _:
                return int(card)

    @property
    def is_five_kind(self) -> bool:
        return 5 in self.card_counts or (
            self.part == 2 and max(self.card_counts_not_joker) + self.joker_count == 5
        )

    @property
    def is_four_kind(self) -> bool:
        return 4 in self.card_counts or (
            self.part == 2 and max(self.card_counts_not_joker) + self.joker_count == 4
        )

    @property
    def is_full_house(self) -> bool:
        return (
            2 in self.card_counts
            and 3 in self.card_counts
            or (
                self.part == 2
                and len([x for x in self.card_counts if x == 2]) == 2
                and self.joker_count == 1
            )
        )

    @property
    def is_three_kind(self) -> bool:
        return 3 in self.card_counts or (
            self.part == 2 and max(self.card_counts_not_joker) + self.joker_count == 3
        )

    @property
    def is_two_pair(self) -> bool:
        # there are 3 cards
        unique_cards = set(self.cards)
        if not len(unique_cards) == 3:
            return False

        counts = [len([x for x in self.cards if x == c]) for c in unique_cards]

        # there are 2 cards with pairs
        return len([c for c in counts if c == 2]) == 2

    @property
    def is_pair(self) -> bool:
        return 2 in self.card_counts or (self.part == 2 and self.joker_count > 0)

    @property
    def type(self) -> int:
        if self.is_five_kind:
            return 6
        if self.is_four_kind:
            return 5
        if self.is_full_house:
            return 4
        if self.is_three_kind:
            return 3
        if self.is_two_pair:
            return 2
        if self.is_pair:
            return 1
        return 0

    @classmethod
    def compare(cls, one, other) -> int:
        if one.type > other.type:
            return 1
        if other.type > one.type:
            return -1

        for i in range(len(one.cards)):
            if one.card_value(one.cards[i]) > other.card_value(other.cards[i]):
                return 1
            if other.card_value(other.cards[i]) > one.card_value(one.cards[i]):
                return -1

        return 0


def parse_hand(line: str) -> Hand:
    cards, bid = line.split(" ")
    return Hand(cards=[c for c in cards], bid=int(bid), part=1)


hands = [parse_hand(line) for line in lines]


# Part 1
print(
    sum(
        hand.bid * (i + 1)
        for i, hand in enumerate(sorted(hands, key=cmp_to_key(Hand.compare)))
    )
)

# Part 2
for hand in hands:
    hand.part = 2


print(
    sum(
        hand.bid * (i + 1)
        for i, hand in enumerate(sorted(hands, key=cmp_to_key(Hand.compare)))
    )
)
