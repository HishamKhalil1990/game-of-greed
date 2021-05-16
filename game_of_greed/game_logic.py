from abc import ABC
class Game_logic():
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(cls,picked_dice:tuple):
        pass

    @staticmethod
    def roll_dice(cls,num_dice:int):
        pass

    def __str__(self):
        pass

class Banker():
    def __init__(self):
        self.shelved = 0
        self.balance = 0
        pass

    def shelf(self,claculated_score:int):
        self.shelved = claculated_score
        pass

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        pass

    def clear_shelf(self):
        pass

