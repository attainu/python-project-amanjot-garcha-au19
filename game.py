from entities.Score import turn
from entities.ladders import Ladders
from entities.numofplayers import Players
from entities.snakes import Snakes
from entities.intro import Intro


class Snake_ladder:
    def __init__ (self):
        pass   

    

    

    def run(self):
        intro = Intro()
        ladders = Ladders()
        players = Players()
        snakes = Snakes()
        intro.printintro()
        while True:
            play = input("Press Enter to Play and Exit to quit the game: ")
            if play == "":
                    snakes.numOfSnakes()
                    ladders.numOfLadders()
                    names = players.playerNames()
                    
                    print("Good Luck!")
                    print()    
                    while True:
                        play2 = input("Press Enter to start.")
                        if play2 == "":
                            player1_score = player2_score = player3_score = player4_score = 0
                            while True:
                                
                                player1_score = turn(names[1],player1_score)
                                if player1_score == 100:
                                    break
                                player2_score = turn(names[2],player2_score)
                                if player2_score == 100:
                                    break
                                if 4 > len(names) > 2:
                                    player3_score = turn(names[3],player3_score)
                                    if player3_score == 100:
                                        break    
                                if 5 > len(names)> 3:
                                    player4_score = turn(names[4], player4_score)
                                    if player4_score == 100:
                                        break
                                print("________________________________________________________________")
                                
                        break                                                
            elif play=="exit" or play=="Exit":
                    break
                # quit

if __name__ == '__main__':
    j = Snake_ladder()
    
    j.run()
    


