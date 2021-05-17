from builtins import tuple
from abc import ABC
from collections import Counter 
import random
from typing import Container

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


class Game:
    def __init__(self,roll_test) :
        self.test_input = roll_test
        

    def play (self):
        counter = 1
        dic_num = 6
        total_score = 0
        shelf_score = 0
        not_quit = True
        print('Welcome to Game of Greed')
        user_input = input('Wanna play?')
        if user_input.lower() == 'n' :
            print('OK. Maybe another time')
        elif user_input.lower()=='y':
           while(not_quit):
                print(f"""Starting round {counter}
Rolling {dic_num} dice...""")
                obj = Game_logic()
                separator = ','
                array = [str(int) for int in obj.roll_dice(dic_num)]
                print( separator.join(array))
            
                # print(self.test_input)
                val =  input('Enter dice to keep (no spaces), or (q)uit:')
                if val.lower() == 'q' :
                    not_quit = False
                    print(f"""Total score is {total_score} points
Thanks for playing. You earned {total_score} points""")    
                else :
                    input_dic = tuple(int(num) for num in val)
                    shelf_score = obj.calculate_score(input_dic)
                    dic_num -= len(input_dic)
                    print(f"You have {shelf_score} unbanked points and {dic_num} dice remaining")
                    user_choice = input('(r)oll again, (b)ank your points or (q)uit ')

                    if user_choice.lower() == 'b' :
                        total_score += shelf_score
                        print(f"""You banked {shelf_score} points in round {counter}
Total score is {total_score} points""")
                        dic_num = 6
                        shelf_score = 0
                    elif user_choice.lower() == 'r':
                        pass
                    elif user_choice.lower() == 'q':
                        not_quit =  False
                        print(f"""Total score is {total_score} points
Thanks for playing. You earned {total_score} points""")  
                    else :
                        print('')
                    counter += 1
        else:
            print('')


# obj = Game()
# obj.play()