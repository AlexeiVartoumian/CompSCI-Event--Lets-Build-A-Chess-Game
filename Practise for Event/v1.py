"""
so our plan of attack is as follows

I know that I will have two main classes. I need a class game to which will belong the functions needed to 
carry out the game. for that we need to ask what is the framework that allows a game of chess to be possible?

1. board. we need board. since we are not going to impelemnt a gui we need to represent the board somehow. well we can do so with strings!
the idea is to "print" an 8 by 8 board. this will be of string data type. building on this our peices will also be strings BUT on the board they will be represeneted as strings.
2. pieces. of course the pieces have thier own functionality which we will discuss later. right now we need to somehow do the following. 1.represent the pieces as strings on our string board. 2. use a suitable data strucuture that enables us to implement the "business logic" of the peices and transform it into strings on the board.
3. a main gameplay. in theory you can play a game of chess forever if its stalemate or whatever. as such for our purposes we shall implemnt some sort of eternal loop that follows a series of checks and switches from player to player. for eg 1. ask user input. 2. validate input against possible moves. 3. if valid then execute move and switch players. which reminds me we also need to a switch player functionality and colours to represent this balck and white.

okay so i think we have the basic functionality of the board covered now we have should discuss the piece functionality.

it is appropriate to use oop because alot of the pieces are foing to share the same functionlity, for example. they will have a position on the board. they will have a list of possible moves. they will have the ability to take an opposing piece which will depend on the colour.
so our apporach is this. we will first make a general class piece. after which we will chef up the functionality of the pawn where moves specific to the pawn will override the general piece class.

the backbone of our approach to building this game is the dictionary/hashmap data structure. this data structure is a key value pair. for our purposes we will set the key to be the i,j cordinates of where our peice will sit on the board. consequenetly the value will be the respective peice class that sits at those co-ordinates. whats really neat about this is that we can package the whole thing up as a dictionary itself; meaning i want to take the above and set it as a value of a super dictionary where the key will be the player as in "WHITE" or "BLACK". this will allow us to validate moves based on whose turn it is, if theres no conflict ext.

as such our step by step approach is as follows!
1. isntantiatie our classes with the variables and functions commented out but implemented later.
2. begin by implementing the board! i would like to see what im doing no?
3. once thats done i would like to see a piece on the board, that means well start cheffing up the piece class
4. then we can start doing the pawn and placing it on the board!
5. keeping in mind that these are classes we will have to have a suitable data structure to where the string rep will have the piece func
 def __repr will do that nicely check it out ont he docs some python sauce for the flavour.

ok i think we have a good base to start with any cases we havent thought of we can impelement and tackle as we go along lets GO!!!
"""

import pdb
#step1 imple late
BLACK = "black"
WHITE = "white"

class Game:

    def __init__(self):
        self.playersTurn = BLACK
        self.message = "future prompts will go here"
        self.gameboard = {}
        self.placePieces() #this will take the gameboard above and print them onto our board we will uncomment this after filling out
        print("moves to be entered in algrabraic expression seprated ny space  for example: e2 e4")
        print(self.gameboard)
        self.main()   #this will handle the gameplay logic
    

    def simulate_input(self,index ): # this function was made to simulate chess moves for a gif so as to promote the event.
        
            inputstring = ["e7 e6"," e2 e3"," b8 c6","f1 c4","g8 f6","g1 f3", "d7 d6","c2 c3","f8 e7","e3 e4", "c6 e5","c4 b3","e8 c6","d2 d3","f6 d5"]
            a,b = inputstring[index].split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            print(a,b)
                #return (a,b)
                 # Simulate user input by yielding the list of words
            return (a,b)
    # now we can comment out our basic funcs for the game class we wont touch any of this until class peice, pawn and unidict is filled out youll see

    def placePieces(self):# after unidict is done we can hanfle this 
        # what is our approacj here? well similar to the print board we need to initially print the peices on the board right?
        # for example  our blacj pawns will start pos 1 of our board and white peices will start at pos 7  and for every such pos
        # we do the following= create a record in the gameboard dict with i, j co-ords  inside tyupleas key and the class as value with respective colour passed in pawns are special case- rememeber how we included direction? here we decalre 1 for black as in its going foraward to 8
        # and -1 for white pawns 
        for i in range(0,8):
            self.gameboard[(i,1)] = Pawn(WHITE,unidict[WHITE][Pawn],1)
            self.gameboard[(i,6)] =Pawn(BLACK,unidict[BLACK][Pawn],-1)

            # we are nearly ready to place the pieces on the board we just have to translate user input so user can actually move the pawns
    def main(self):
        # after placepeice parseintput has been done. we basically have an infiniite loop her.and do the following
        # step 1print board , accept user input , then validate user input which means the following: 
        # step 2 check if first half of user input is a position on the gameboard dictionary use a try block for that. if not throw error message could not ind peice
        # step 3 validate second half of user input and see hey is that valid target; use if else to validate that. 
        # step 4 then we have to see if the correct colour piece has been chosen . if not then invalid move.
        # step 5 we can now finally validate if the user move is valid according to functionality of peice! if valid move then update dictionary to the end position cor-ords.
        # step 6 we will check if a check has been made and then finally siwtch player turn. keep in mind if isvalid returns false then start whole process again
        while True:
            self.printBoard()
            print(self.message)
            self.message = ""
            startposition,endposition = self.parseInput()
           
            try:
                target = self.gameboard[startposition]
                print(target, "hahahaa")
            except:
                self.message = "could not find peice "
                target = None

            if target:
                    print("found "+str(target))
                    if target.Color != self.playersTurn:
                        self.message = "not allowed to move that peice that turn"
                        continue
                    if target.isValid(startposition,endposition,target.Color,self.gameboard): 
                        self.message = "this is a valid move"
                        self.gameboard[endposition] = self.gameboard[startposition]
                        del self.gameboard[startposition]
                        #self.ischeck()

                        if self.playersTurn == BLACK:
                            self.playersTurn = WHITE
                        else:
                            self.playersTurn = BLACK
                    else:
                        print("invalid move" + str(target.availablemove(startposition[0],startposition[1],self.gameboard)))
            else:
                    self.message = "ther is no piece on tha board"
            

    def parseInput(self):
        """
        we are going to be doing alot of validated here so a try except block if useful: all that does is if an eroor is thrown then program wont crash and will continue to execute. we need this toi maintain state of game
        as such remember at the v beginging we said we accpet e4 e6 as notation? well our approach will be to do this: split the input according to space. turn them into tuples where first part is coonvered from letter to digit and the sceond part is oconverted to integer -1 to account for zero based board. finally return output if valid. if some weird shit happens then return except is thrown and we reutrn (-1,-1)
        """
        try:
            a,b = input().split()
            #a = ((ord(a[0]))-97),int(a[1],-1)
            #b = (ord(b[0])-97,int(b[1]),-1)
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            print(a,b)
            return (a,b)
        except:
            print("hey something strange  happened try again")
            return ((-1,-1),(-1,-1))
        # so we have parsed input we have our pawns in string rep ready to go. its not time to implement the main loop! uncomment that 

    def printBoard(self): 

        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")

        """
        so our logic for printing the board is as follows from we will for every row do the following.
        take the i + 97 letter on the ascii chart
        then print the a relevant piece on the board. for now we will use our dictionary class and grab the respective co-ordinates
        from there but it that wont do anything which is ok we just want the board
        print a bunch of dashes follwed by a delimiter at the end.
        repeat process up to eight times. alright lets go!
        """
        for i in range(0,8):
            print("-" * 32)# trial and error trial and error

            # now we are going to fill out the center! that means hey for every row we will now do the following 
            # print the letter as  discussed above  the i j co ordinates of a peice if it exists and the a delimiter!
            print(chr(i+97), end= "|")
            for j in range(0,8):
                item = self.gameboard.get((i,j)," ")
                print(str(item)+ " |" ,end = " ") # remember we want the string representation
            print()
            print("-" * 32)
            

class Piece:
    # this is the shared behaviour class here we will implment the shard funcs all pieces will inherit and override
    def __init__(self, color,name):
        self.Color = color
        self.name = name
        self.position = None

    def isValid(self, startposition,endposition,Color,gameboard): # we need to check  if given coordinates of a piece obey the rules of chess so we need some parameters but before we do this we will implement no conflict class to see how our data is structured in the dictionary
    
        if endposition in self.availablemoves(startposition[0],startposition[1],gameboard,Color = Color):
            return True # after noconflict func completed we are basically sanitising the user input against available moves which will be detailed specifically in the unique pieces
        return False
        # alright now we can start cheffing up our unique piece classes!  we begin witrh pawn

    def __repr__(self):
        return str(self.name) # this is going to allow us to represent our base class in a string form
    
    def __str__(self):
        return str(self.name)
    
    def availablemoves(self,x,y,gameboard):
        # indi classes will take theier x y co-ords and according to thier move rules this func will calc poss moves in tuple form
        print("no movement allowed for base class")


    
    #def adNauseam(self, x, y, gameboard,Color, intervals): # peices like rook and queen and bishop will have repreated moves forever right?

    def isinbounds(self, x ,y): # here we simplay check if the i j co-ords respect out 8 by 8 board

        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    # we have checked if a piece is in board. now we have to check it doesnt violate the rules right?

    def noConflict(self, gameboard, initialColor, x, y):# we will need follow params - the co-ords the color the and the current state of the gameboard
        # now we check hey are we in bounds? then grab co-ords from dictionatry and use the params plus abailbal moves to see if we our piece obey the game of chess
        if(self.isinbounds(x,y) and ((x,y) not in gameboard or gameboard[(x,y).Color] != initialColor)):
            return True
        # this is the beautiful part becaus ewe used a dcitanary with tuple inside of which is the co-ords as key and Piece class as value  
        return False

        # okauy lets go back to the isvalid class! we shown how we are representing our pieces on the board within the gameboard dictionary, now we can validate a move according to the following if user input end pos is iin poss moves and 


class Pawn(Piece): #with oop we can pass in other classes into our class. v useful for implementing our game logic!

    # okay now we can finally start making the individual funcs of our class . pawns are unique in the game in that they can be 
    # promoted- forget aboutit not doing that now.
    # enpassant; some french shit forget about it
    # they take opposing peices diagonally and they move in a certain direction.
    # lets begin taking the above and chucking it into a  constructor

        def __init__(self,color,name,direction):
            self.name = name
            self.Color= color
            self.direction = direction
    
        # keep in mind that direction will be defined by user input which we will validate with our availble moves func
        
        def availablemoves(self,x,y,gameboard,Color = None):
            if Color is None:
                Color = self.Color
            
            answers = []

            # we have three cases to consider moving forward, taking diagonally and finally the same for opp direction right?
            if (x+ 1, y + self.direction) in gameboard and self.noConflict(gameboard,Color,x+1,y+self.direction):
                answers.append((x+1,y+self.direction))
            
            if(x-1,y+self.direction) in gameboard and self.noConlict(gameboard,Color,x-1,y+self.direction):
                answers.append((x-1,y+self.direction))
            
            #just norm pawn move
            if(x + y+ self.direction) not in gameboard and Color == self.Color:
                answers.append((x, y +self.direction))
            
            return answers
            
    #okay now we can go ahead and go into google to grab our ascii peices! we need them because we will implement our dictionary hahaha

              
unidict= {WHITE:{Pawn: "♙"},BLACK:{Pawn:"♟︎"}}

# after finally implementing the our dicitonary of class piece to string representation we can go ahead and represent this on the on our print board -- that means going back to main class and fillig out the placepeice functiion 
    
#morething = "♖	♘	♗	♕	♔	♗	♘	♖"

#morethingbalck = "♜	♞	♝	♛	♚	♝	♞	♜"

# for testing purps we will call game class plus method
#   

Game()