from random import randint
from collections import Counter


class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return tuple([randint(1,6) for _ in range(num_dice)])

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
            elif die == 1 and count == 5:
                score += 4100
            elif die == 1 and count == 6:
                score += 4200
            elif count == 3:
                score += score_dict[die]
            elif count == 4:
                score += score_dict[die] * 2
            elif count == 5:
                score += score_dict[die] * 3
            elif count == 6:
                score += score_dict[die] * 4

        return score

        # score = 0
        # counts = Counter(values)
        # pair_counter = 0
        #
        # for die in counts:
        #     if counts[die] == 2:
        #         pair_counter += 1
        #     if pair_counter < 3 and len(counts) < 6:
        #         if die == 1:
        #             if counts[die] == 1:
        #                 score += 100
        #             elif counts[die] == 2:
        #                 score += 200
        #             elif counts[die] == 3:
        #                 score += 1000
        #             elif counts[die] == 4:
        #                 score += 2000
        #             elif counts[die] == 5:
        #                 score += 3000
        #             elif counts[die] == 6:
        #                 score += 4000
        #         if die == 2:
        #             if counts[die] == 1:
        #                 score += 0
        #             elif counts[die] == 2:
        #                 score += 0
        #             elif counts[die] == 3:
        #                 score += 200
        #             elif counts[die] == 4:
        #                 score += 400
        #             elif counts[die] == 5:
        #                 score += 600
        #             elif counts[die] == 6:
        #                 score += 800
        #         if die == 3:
        #             if counts[die] == 1:
        #                 score += 0
        #             elif counts[die] == 2:
        #                 score += 0
        #             elif counts[die] == 3:
        #                 score += 300
        #             elif counts[die] == 4:
        #                 score += 600
        #             elif counts[die] == 5:
        #                 score += 900
        #             elif counts[die] == 6:
        #                 score += 1200
        #         if die == 4:
        #             if counts[die] == 1:
        #                 score += 0
        #             elif counts[die] == 2:
        #                 score += 0
        #             elif counts[die] == 3:
        #                 score += 400
        #             elif counts[die] == 4:
        #                 score += 800
        #             elif counts[die] == 5:
        #                 score += 1200
        #             elif counts[die] == 6:
        #                 score += 1600
        #         if die == 5:
        #             if counts[die] == 1:
        #                 score += 50
        #             elif counts[die] == 2:
        #                 score += 100
        #             elif counts[die] == 3:
        #                 score += 500
        #             elif counts[die] == 4:
        #                 score += 1000
        #             elif counts[die] == 5:
        #                 score += 1500
        #             elif counts[die] == 6:
        #                 score += 2000
        #         if die == 6:
        #             if counts[die] == 1:
        #                 score += 0
        #             elif counts[die] == 2:
        #                 score += 0
        #             elif counts[die] == 3:
        #                 score += 600
        #             elif counts[die] == 4:
        #                 score += 1200
        #             elif counts[die] == 5:
        #                 score += 1800
        #             elif counts[die] == 6:
        #                 score += 2400
        # if pair_counter == 1 and counts[die] == 3:
        #     score = 1500
        # if pair_counter == 3:
        #     score = 1500
        # if len(counts) == 6:
        #     score = 1500
        # return score


        # find count of each number rolled

        # if count is 3: score is number times 100
            # else if it's three 1s: 1000 points
            # else if there are 3 of a kind and a pair: 1500 points

        # if count is 4: score is number times 100 times 2
            # else if it's four 1s: 2000 points

        # if count is 5: score is number times 100 times 4
            # else if it's five 1s: 4000 points

        # if count is 6: score is number times 100 times 8
            # else if it's six 1s: 8000 points

        # if count < 3: determine if number is a 1 or 5
            # if 1: each 1 is worth 100 points
            # if 5: each 5 is worth 50 points
            # else if there are three pairs: 1500 points
            # else if there's a straight 1-6: 2000 points
            # else: 0 points


