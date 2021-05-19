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
    
    @staticmethod
    def validate_keepers(roll, keepers):
        counter_one = Counter(keepers)
        output_one= counter_one.most_common()
        counter_two = Counter(roll)
        output_two = counter_two.most_common()
        result=[]
        for num_2 in output_two:
            for num_1 in output_one:
                if num_1[0] == num_2[0]:
                    if num_1[1] <= num_2[1]:
                        result.append(1)
        if not len(result) == len(output_one):
            return False
        else :
            return True

    @staticmethod
    def get_scorers(test_input):
        counter = Counter(test_input)
        output = counter.most_common()
        if len(output) == 6:
            return test_input
        elif len(output) == 3:
            if output[0][1] == 2 and output[1][1] == 2 and output[2][1]==2:
                return test_input
            else:
                return Game_logic.get_score_sub(output)
        else:
            return Game_logic.get_score_sub(output)

    @staticmethod
    def get_score_sub(test_input):
        output = []
        for dice in test_input:
            if dice[1] == 6:
                for item in range(6):
                    output.append(dice[0])
                    
            elif dice[1] == 5:
                for item in range(5):
                    output.append(dice[0])
            elif dice[1] == 4:
                for item in range(4):
                    output.append(dice[0])
            elif dice[1] == 3:
                for item in range(3):
                    output.append(dice[0])
            elif dice[1] == 2:
                if dice[0] == 1:
                    for item in range(2):
                        output.append(dice[0])
                elif dice[0] == 5:
                    for item in range(2):
                        output.append(dice[0])
            elif dice[1] == 1:
                if dice[0] == 1:
                    for item in range(1):
                        output.append(dice[0])
                elif dice[0] == 5:
                    for item in range(1):
                        output.append(dice[0])
        return output 

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
