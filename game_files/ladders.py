from snakes import Snakes
snks = Snakes()

class Ladders(Snakes):
    def __init__(self):
        self.ladders = {}
        
        
        Snakes.__init__(self)
    

    def numOfLadders(self):
        self.ladders = {}
        snksdict = snks.checkForSnakes(0)
        # calling snakes class from ladders so its easier to 
        # check later in function that snakes and ladders dont make an "infinite loop" in line # 59
        print()
        while True:
            print ("   okayyy next lets  pick number of ladders you want on your board  ")
            num_of_ladders = (input("    pick a number between 1 to 10 :"))
            try:                    # to handle incorrect input by user e.g. "string"
                int(num_of_ladders) 
                # flag = True
                
            except:
                print()
                print(" ooops wrong Input   ")
                print()
                continue
            num_of_ladders = int(num_of_ladders)
            if 11 > num_of_ladders > 0 :
                print()

                print("Enter Start and End separated by a space")

                i = 0

                while i < (num_of_ladders):
                    flag = 0
                    
                    first = input("\n Start and End :  ").strip().split()
                    if len(first) != 2:# to handle invalid input by user
                        print()
                        print(" oops wrong input ")
                        print()
                        print(" Enter Start and End separated by a space")
                        continue
                    try :   # to handle "string" input by user
                        int(first[0])
                        int(first[1])
                    except:
                        print()
                        print("  oops wrong input  ")
                        print(" Enter start and end separated by a space")
                        continue
                    start = int(first[0])
                    end   = int(first[1])



                    if start > 0 and end < 100:

                        if end <= start:
                            print("\n The end should be greater than Start")
                            flag = 1
                            i -= 1
                        elif start in self.ladders.keys():
                            print("\n Ladder already present")
                            flag = 1
                            i -= 1
                        
                        for k, v in snksdict.items(): # to check snakes and ladders dont form an "infinite loop"
                            
                            if k == end and v == start:
                                print("\nSnake present at 'end' box with its 'tail' at 'start' box (will create infinite loop)")
                                print("\nPlease Enter different start and end for  Ladder")
                                flag = 1
                                i -= 1

                        else:
                            if flag == 0:
                                self.ladders[start] = end
                                

                            else:
                                pass

                        i += 1

                    else:
                        print(" ohh noo !!!  kindly choose b/w 0 to 100")

                print("\n  bingo!!!!!  Your Ladders are at: ", self.ladders, "\n")

            else:
                self.numOfLadders()
            
            return self.ladders
        
    nums = {}
    def checkForladders(self, score):
        global nums
        if score == 0:# making sure when this function is called for taking input from user for ladders only first half of function
                       # executes
            
            nums = self.numOfLadders() 
            # calling numOfLadders function from inside checkForLadders to make sure values in nums are synchronised
            # with values inputed by user in self.ladders
            
        if score != 0:  # for making sure when function is called from score to check if a ladder is present at a specific box 
                       # only second half of function is executed
            if score in nums.keys():
                
                
                return nums[score]

            else:
                return score



    