from game_of_greed.game_logic import *

class Game:

    def __init__(self) :
        pass
        self.test_input = None

    def play (self,roller = None):
        self.test_input = roller or Game_logic.roll_dice
        counter = 1
        dic_num = 6
        total_score = 0
        shelf_score = 0
        not_quit = True
        not_skip = True
        print("""Welcome to Game of Greed
(y)es to play or (n)o to decline""")
        user_input = input('> ')
        if user_input.lower() == 'n' :
            print('OK. Maybe another time')
        elif user_input.lower()=='y':
            print(f"Starting round {counter}")
            while(not_quit):
                separator = ' '
                array = [str(int) for int in self.test_input(dic_num)]
                check = False
                print(f"Rolling {dic_num} dice...")
                if Game_logic.calculate_score(tuple(int(string) for string in array)) != 0:
                    while not check:
                        print("*** " + separator.join(array) +" ***")
                        val =  input("""Enter dice to keep, or (q)uit:
> """)
                        if val.lower() == 'q' :
                            not_quit = False
                            print(f"Thanks for playing. You earned {total_score} points")  
                            break
                        else :
                            input_dic = tuple(str(num) for num in val if num != " ")
                            check= Game_logic.validate_keepers(array , input_dic)
                            if not check :
                                print("Cheater!!! Or possibly made a typo...")  
                else:
                    print("*** " + separator.join(array) +" ***")
                    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                    not_skip = False
                    user_choice = 'b' 
                    total_score = 0
                    shelf_score = 0
                if not_quit :
                    if not_skip:
                        input_dic = tuple(int(num) for num in input_dic)
                        shelf_score = Game_logic.calculate_score(input_dic)
                        dic_num -= len(input_dic)
                        print(f"You have {shelf_score} unbanked points and {dic_num} dice remaining")
                        print("(r)oll again, (b)ank your points or (q)uit:")
                        user_choice = input("> ")
                    if user_choice.lower() == 'b' :
                        total_score += shelf_score
                        not_skip = True
                        print(f"""You banked {shelf_score} points in round {counter}
Total score is {total_score} points""")
                        dic_num = 6
                        shelf_score = 0
                        counter += 1
                        print(f"Starting round {counter}")
                    elif user_choice.lower() == 'r':
                        pass
                    elif user_choice.lower() == 'q':
                        not_quit =  False
                        print(f"Thanks for playing. You earned {total_score} points")  
                    else :
                        print('')
                    if dic_num == 0:
                        dic_num = 6    
                    
        else:
            print('')

if __name__ == '__main__':
    game = Game()
    game.play(None)
