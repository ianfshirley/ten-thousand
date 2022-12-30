from random import randint
from collections import Counter


class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return tuple([randint(1, 6) for _ in range(num_dice)])

        # line above does the same thing as this code block:

        # values = []
        # for i in range(num_dice):
        #     value = randint(1, 6)
        #     values.append(value)
        # return tuple(values)

    @staticmethod
    def calculate_score(dice_roll):
        dice_count = Counter(dice_roll)
        score = 0
        score_dict = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

        # straight
        if len(dice_count) == 6:
            return 1500

        # three pairs
        if len(dice_count) == 3 and all(value == 2 for value in dice_count.values()):
            return 1500

        for die, count in dice_count.items():
            if die == 5 and count <= 2:
                score += 50 * count
            elif die == 1 and count <= 2:
                score += 100 * count
            elif count == 3:
                score += score_dict[die]
            elif count == 4:
                score += score_dict[die] * 2
            elif count == 5:
                score += score_dict[die] * 3
            elif count == 6:
                score += score_dict[die] * 4

        return score
