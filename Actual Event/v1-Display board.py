
    

"""

so we want to buld a chess game. before we jump in we have to consdeir and reason about how we shall approach building the game.

as such i think a good start to doing so will be to define what makes a game of chess and what is required for a game of chess to

be possible?

as such we begin by listing what we shall need :

BOARD! we need a board on which to play on! that means an 8 by 8 virtual representation is required.



Players! we need players! two players to be precise for one of which will control the balck pieces and the other the white pieces



PIECES! we need pieces, each of which of thier own unqiue functionality thay enable us toplay the game.



RULES! we will define the rules of chess as the minimum set of requirements needewd in order for us to play the game

for example:

1. all pieces must start on an intital and correct place on the board.

2.each player is to take their turn using algrebraic notation to make a move sequentially in respect to the other player: in which a process must occur tbd later

3.each peice according to its UNIQUE moving functionality must respect the boundaries of the board and the moves which it can execute, which means we must determine how and where a given piece can move and will not be able to move.



our rules above are somewhat generalised and so we will address this by categorise the above in different buckets so to speak according to how similar the operations are to each other. we shall use  classes for this which we can think of as data types to which belong shared functionality.



well suppose we have two such classes where the game functionality can be a class, and the piece functionality can be a class.



building on this we can attribute the board player turn, player input gameboard persistence and overall structure of the game to the game class. and we can attribute all the shared behaviour of a given piece i.e abvaliable moves, does it respect the board, is an opposing piece to be taken actually of a different colour to a piece class.



finally before we begin we should discuss how we should represent the board and the peices. well for our purposes a suitable option is strings; strings tro represent the board . and strings to represent the class functionality. we shall do so with a key value pair data structure, where the base case will be the Colour as key, Piece CLASS as value

e and then to enable the gameplay  we will have inner key value pair data sttrucure where the algebraic notation of a unique peice will be the key as in ( 4,6) --> we wil use string manipulation to handle converting user input from say "e4 e6 to" 4 6 to update a player move, the point being we will have a gameboard hashmap storing all the key value pairs of all the peices on the board. finally we will use an eteranl while loop belonging to the game class that will update the board at every user input. if the above sounds a little convoluted then it is, lets just say we want to use a key value pair data structure where that will do two things, remember the state of the board and the associate who can move where.



so where do we begin?? lets begin by palcing all the varaibles discussed above in our bucket classes an then start by print oru board. alright now lerts go!

"""
    

BLACK = "black"

WHITE = "white"


"""
step 1: printboard

step2 : handle general peice funcionaltty

ste3: handle pawn class

step4 place that peice on the board

"""

class Game():
    def __init__(self):

        self.playersturn= BLACK
        self.message= ""
        self.gameboard = {}
       #self.placePiece()
       ##self.main()


    #def placePiece(self):



    #def main(self):



    #def parseInput(self):



    print("please enter an viable algebaric expression  for example e7 e6")



    def printBoard(self):

                print("  1 | 2 | 3 | 4 | 5 | 6 | 8 |")

                # we need an 8 by 8 board

                for i in range(0,8):

                        print("-"* 32)

                        print(chr(i+97), end="|")

                        for j in range(0,8):

                                item = self.gameboard.get((i,j), " ")

                                print(str(item)+ " |", end = " ")





                        print()

                        print("-"* 32)



#class Piece():



Game().printBoard()

