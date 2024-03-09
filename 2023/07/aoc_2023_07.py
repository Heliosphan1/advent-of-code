# Advent of Code - 2023 - day 7
from collections import Counter
from functools import total_ordering

"""
5 > 4 > 3+2 > 3 > 2+2 > 2 > 1
"""

def solve_part_one():
    @total_ordering
    class CardHand():
        
        value_map = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }
        
        def __init__(self, s: str):
            self.hand = s
            self.card_count = Counter(s)
            self.value_set = set(self.card_count.values())
            self.strength = self.get_strength()
            
        def __repr__(self):
            return self.hand 
        
        def get_strength(self):
            if 5 in self.value_set:
                return 7
            elif 4 in self.value_set:
                return 6
            elif 3 in self.value_set:
                if 2 in self.value_set:
                    return 5
                else:
                    return 4
            elif 2 not in self.value_set:
                return 1
            elif len(self.card_count) == 3:
                return 3
            else:
                return 2
        
        def __eq__(self, other):
            return self.hand == other.hand 

        def __lt__(self, other):
            if self.strength == other.strength:
                for card_s, card_o in zip(self.hand, other.hand):
                    value_s = CardHand.value_map.get(card_s)
                    value_o = CardHand.value_map.get(card_o)
                    if value_s == value_o:
                        continue
                    else:
                        return value_s < value_o
                return False
            else:
                return self.strength < other.strength 

    data = []
    with open("input.txt") as input_file:
        for line in input_file.readlines():
            hand, bet = line.strip('\n').split(' ')
            hand = CardHand(hand)
            data.append((hand, int(bet)))

    data.sort(key = lambda x: x[0])
    s = sum((bet * (rank + 1) for rank, (hand, bet) in enumerate(data)))
    print(s)

def solve_part_two():
    @total_ordering
    class CardHand():
        
        value_map = {
            'J': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'Q': 12,
            'K': 13,
            'A': 14
        }
        
        def __init__(self, s: str):
            self.hand = s
            self.card_count = Counter(s)
            self.j_count = self.card_count.get('J', 0)
            self.value_set = set(self.card_count.values())
            self.strength = self.get_strength()
            
        def __repr__(self):
            return self.hand 
        
        """5 > 4 > 3+2 > 3 > 2+2 > 2 > 1"""
        
        def get_strength(self):
            if 5 in self.value_set: # 5 of the same card
                return 7
            elif 4 in self.value_set: # 4 + 1
                if self.j_count > 0: # 5 of the same card
                    return 7 
                else: # 4 + 1
                    return 6
            elif 3 in self.value_set: # 3 + 1 + 1
                if 2 in self.value_set: # 3 + 2
                    if self.j_count > 0: # 5 of the same card
                        return 7
                    else: # 3 + 2
                        return 5
                else: # 3 + 1 + 1
                    if self.j_count > 0: # 4 + 1
                        return 6
                    else: # 3 + 1 + 1
                        return 4 
            elif 2 not in self.value_set: # 1 + 1 + 1 + 1 + 1
                if self.j_count > 0: # 2 + 1 + 1 + 1
                    return 2
                else: # 1 + 1 + 1 + 1 + 1
                    return 1
            elif len(self.card_count) == 3: # 2 + 2 + 1
                if self.j_count == 2: # 4 + 1
                    return 6
                elif self.j_count == 1: # 3 + 2
                    return 5
                else: # 2 + 2 + 1
                    return 3
            else: # 2 + 1 + 1 + 1
                if self.j_count > 0: # 3 + 1 + 1
                    return 4
                else: # 2 + 1 + 1 + 1
                    return 2
        
        def __eq__(self, other):
            return self.hand == other.hand 

        def __lt__(self, other):
            if self.strength == other.strength:
                for card_s, card_o in zip(self.hand, other.hand):
                    value_s = CardHand.value_map.get(card_s)
                    value_o = CardHand.value_map.get(card_o)
                    if value_s == value_o:
                        continue
                    else:
                        return value_s < value_o
                return False
            else:
                return self.strength < other.strength
            
    data = []
    with open("input.txt") as input_file:
        for line in input_file.readlines():
            hand, bet = line.strip('\n').split(' ')
            hand = CardHand(hand)
            data.append((hand, int(bet)))

    data.sort(key = lambda x: x[0])
    s = sum((bet * (rank + 1) for rank, (hand, bet) in enumerate(data)))
    print(s)

solve_part_two()