
from random import randint
from ladders import Ladders
from snakes import Snakes
import time

ladders = Ladders()
snakes = Snakes()

def turn(player,score): #Turn function
    delay = .05
    while True:
        print("Its  ",player,"'s  turn ")
        time.sleep(delay)
        print()
        roll2 = input("Press enter to Roll ")
        time.sleep(delay)
        print()
        if roll2 == "":
            a=randint(1,6)#player dice roll
            print(player,"rrrolled the dice")
            time.sleep(delay)
            
            print(player,"got a  ",a)
            
            time.sleep(delay)
            newscore = score + a 
            if newscore < 100 :
                print(player, " moved from ", score, " to ", newscore)
                print()
        else:              # to handle user pressing a key other than "enter"

            print()
            print(" oops wong input  ")
            time.sleep(delay)
            print()
            continue


        score  += a
        
        if score <= 100:
            
            lad = ladders.checkForladders(score) #checking for ladders for player
            
            if lad != score:
                print("hurraayy there's a ladder on  ",score, "  ",player,"climbed up to box ", lad)
                time.sleep(delay)
                print()
                score = lad
            snk = snakes.checkForSnakes(score)
            if snk != score: #checking for snakes for player
                print("oooops there's a venomous snake on box ", score, "  ",player,"fell down to box ", snk)
                time.sleep(delay)
                
                score = snk
            print(player,"is now on box  ",score)   
            time.sleep(delay)
            print() 
        else: #checks if player score is not greater than 100
            score -= a
            print(player,"can't move.  ")
            time.sleep(delay)
            print()
            print(player,"is still on box  ",score)
        if score == 100:
            print()
        
            print("hurrrraaayyyyy    ",  player ,"                 Wins!!!!!                ")
        return score