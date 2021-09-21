from Score import turn
from ladders import Ladders
from numofplayers import Players
from snakes import Snakes
from intro import Intro
import time


class Snake_ladder:
    def __init__ (self):
        self.delay = .10

    

    

    def run(self):
        intro = Intro()
        ladders = Ladders()
        players = Players()
        snakes = Snakes()
        intro.printintro()
        while True:
            play = input("Press Enter to Play and Exit to quit the game: ")
            play = play.lower()
            
            if play != "" and play != "exit" : # to handle invalid or other "string " input by user 
                print()
                print(" thats not what i was expecting !!!! (:(:")
                print()
                continue
            if play == "":
                    time.sleep(self.delay)
                    print()
                    print("           yyyeahh  let get   going      !!!!!!!      ")
                    time.sleep(self.delay)
                    print()
                    print(" this game is so cool that it lets you pick number of snakes and ladders you want in in ")
                    print("   and!!!  even  where you want them ????  ")
                    time.sleep(self.delay)
                    print()
                    ladders.checkForladders(0)#for inputting snakes and ladders from user 
                    names = players.playerNames()# for inputting player names from user
                    time.sleep(self.delay)
                    print()
                    print("Good Luck!")
                    time.sleep(self.delay)
                    print()    
                    # while True:
                    while True:
                        play2 = input("Press Enter to get rrrrolling!!!!!   ")
                        print()
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
                        else:
                            time.sleep(self.delay)
                            print("  thats not what i was expecting !!!! (:(:  ")
                            print()
                            continue
                        time.sleep(self.delay)
                        print()
                        break
                        # play = input("Press Enter to Play and Exit to quit the game: ")
                        # play = play.lower()

                        
                    continue
                   
            if play=="exit" :
                print()
                time.sleep(self.delay)
                print( "                                exiting                         ")
                time.sleep(self.delay)
                print()
                print("                                  game                          ")
                time.sleep(self.delay)
                print()
                print("                               bye   bye   !!!!                   ")
                print()
                quit()   
            # self.run()# to restart game if user presses "enter" instead of "exit"
if __name__ == '__main__':
    j = Snake_ladder()
    
    j.run()
    


