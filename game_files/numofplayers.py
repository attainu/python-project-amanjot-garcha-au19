class Players:
    def __init__ (self):
        self.players = {}
        self.mode = None
    
    
            
    def numOfPlayers(self):   
        while True:  
            print("Choose your mode (Single player/Multiplayer)")#mode selection
            self.mode = input("Enter 'S' for Single player and 'M' for Multiplayer: ")
            self.mode = self.mode.lower()
            if self.mode != "s" and self.mode != "m":
                print()
                print(" thats not what i was expecting !!!! (:(:")
                print()
                continue
            if self.mode == "s":
                
                num_players = 1
                return num_players
            

            
            else:
                while True:
                    num_players = (input("Enter number of players: "))
                    print()
                    try:                    # to handle incorrect input by user e.g string
                        int(num_players) 
                
                
                    except:
                        print()
                        print(" ohhh no  not agaaain wrong input ")
                        print("Number of players can be between 2 to 4 only ")
                        print()
                        continue
                    num_players = int(num_players)
                    if 1 < num_players < 5 : 
                        # to make sure there is no more than 4 players and atleast 2 players for a multiplyer mode
                        return num_players
                        
                    else:
                        print("Number of players can be between 2 to 4 only ") 
                        print()


         
           
    def playerNames(self):
        nums = self.numOfPlayers()
        #calling numOfPlayers from inside playerNames for synchronisation of values input by user in both the 
        while True:
            self.players[1] = input("Enter Player 1 name:  ")
            if self.players[1] == "": # handling a exception where enters no name 
                print()
                print( "okaaay  anonymous players not alllowed here , please pick a name"  )
                continue
            else:
                break

        if self.mode == "s" :
            
            self.players[2] = "Computer" # for single mode second player is automatically choosen a "computer"
        else:
            while True:
                
                self.players[2] = input("Enter player 2 name: ")
                if self.players[2] == "":
                    print()
                    print( "okaaay  anonymous players not alllowed here , please pick a name"  )
                    continue
                else:
                    break

            if 5 > nums > 2:
                while True:
                    self.players[3] = input("Enter player 3 name: ")
                    if self.players[3] == "":
                        print()
                        print( "okaaay  anonymous players not alllowed here , please pick a name "  )
                        continue
                    else:
                        break


            if 5 > nums > 3:
                while True:
                    self.players[4] = input("Enter player 4 name: ")
                    if self.players[4] == "":
                        print()
                        print( "okaaay  anonymous players not alllowed here , please pick a name  "  )
                        continue
                    else:
                        break

            
        return self.players