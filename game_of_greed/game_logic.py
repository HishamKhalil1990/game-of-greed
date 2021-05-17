from builtins import tuple
from abc import ABC
from collections import Counter 
import random

class Game_logic():
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(picked_dice:tuple):
        counter = Counter(picked_dice)
        output = counter.most_common()
        score = 0
        if len(output) == 6:
            return 1500
        elif len(output) == 3:
            if output[0][1] == 2 and output[1][1] == 2 and output[2][1]==2:
                return 1500
            else:
                return Game_logic.calculated_sub(output,score)
        else:
            return Game_logic.calculated_sub(output,score)
  
    @staticmethod
    def calculated_sub(output,score):
        for dice in output:
            if dice[1] == 6:
                if dice[0] == 1:
                    score += 4000
                else:
                    score += dice[0]*400
            elif dice[1] == 5:
                if dice[0] == 1:
                    score += 3000
                else:
                    score += dice[0]*300
            elif dice[1] == 4:
                if dice[0] == 1:
                    score += 2000
                else:
                    score += dice[0]*200
            elif dice[1] == 3:
                if dice[0] == 1:
                    score += 1000
                else:
                    score += dice[0]*100
            elif dice[1] == 2:
                if dice[0] == 1:
                    score += 200
                elif dice[0] == 5:
                    score += 100
            elif dice[1] == 1:
                if dice[0] == 1:
                    score += 100
                elif dice[0] == 5:
                    score += 50
        return score 

    @staticmethod
    def roll_dice(num_dice:int):
        return tuple(random.randint(1,6) for num in range(0,num_dice))

    def __str__(self):
        pass

class Banker():
    def __init__(self):
        self.shelved = 0
        self.balance = 0

    def shelf(self,claculated_score:int):
        self.shelved = claculated_score

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0

    def clear_shelf(self):
        self.shelved = 0

    def __str__(self):
        pass

