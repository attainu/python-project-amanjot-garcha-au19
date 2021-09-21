class Snakes:

    def __init__ (self):
        self.snakes = {}


    def numOfSnakes(self):
        self.snakes = {}
        while True:
            
            print ("  okayyyy  lets start by picking number of 'snakes' you want on your board ")
            num_of_snakes = (input(" pick a number between 1 to 10:  "))
            try:                    # to handle incorrect input by user
                int(num_of_snakes) 
                # flag = True
                
            except:
                print()
                print(" oops wrong  Input  ")
                print()
                continue

            num_of_snakes = int(num_of_snakes)
            if num_of_snakes > 0 and num_of_snakes < 11: # limiting the number of snakes to 10 to make sure game is working smoothly
                print(" Enter Head and Tail separated by a space")
                i = 0
                while i < (num_of_snakes):
                    first = input("\n head and tail :  ").strip().split()
                    if len(first) != 2  : # to handle invalid input by user (No space or more than 2 numbers)
                        print()
                        print("oops wrong Input")
                        print()
                        print(" Enter head and tail separated by a space")
                        continue
                    
                    try :   # to handle "string" input by user
                        int(first[0])
                        int(first[1])
                    except:
                        print()
                        print("  oops thats not what i expected   ")
                        print(" Enter head and tail separated by a space")
                        continue
                    head = int(first[0])
                    tail  = int(first[1])
                    # head, tail = map(int, input("\n Head and Tail: ").split())
                    
                    if head <= 100 and tail > 0:

                        if tail >= head:
                            print("\n The tail of snake should be less than head")
                            i-=1

                        elif head == 100:
                            print("\n Snake not possible at position 100.")
                            i-=1

                        elif   head in  self.snakes.keys():
                            print("\n A snake already exists at this cell , please pick new number ")
                            i-=1

                        else:
                            self.snakes[head] = tail

                        i += 1
                    else:
                        print("Invalid! kindly choose b/w 0 to 100")

                print("\n Your Snakes are at : ", self.snakes, "\n")
                print()

            else:
                print()
                print()
                self.numOfSnakes()
                

            return self.snakes
    num = {}
    def checkForSnakes(self, score):
        global num
        if score == 0: # making sure when this function is called for taking input from user for snakes only first half of function
                       # executes
            
            num = self.numOfSnakes()
            # calling numOfLadders function from inside checkForSnakes to make sure values in num are synchronised
            # with values inputed by user in self.snakes
        
        if score != 0: # for making sure when function is called from score to check if a snake is present at a specific box 
                       # only second half of function is executed
            if score in num.keys():

                return num[score]

            else:
                return score
        
        return num