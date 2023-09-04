BLACK = "black"
WHITE = "white"
"""
step4 place that peice on the board
step 5 build our key value pairs of pieces 
step 6 represent those pieces on the board
"""
class Game():
        def __init__(self):
                self.playersturn= BLACK
                self.message= ""
                self.gameboard={}
                self.placePiece()
                #self.main()
        
        def placePiece(self):
                for i in range(0,8):
                        self.gameboard[(i,1)] = Pawn(WHITE,unidict[WHITE][Pawn],1)
                        self.gameboard[(i,6)] = Pawn(BLACK,unidict[BLACK][Pawn],-1)
        #def main(self):
        #def parseInput(self):
        print("please enter an viable algebaric expression  for example e7 e6")
        def printBoard(self):
                print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
                # we need an 8 by 8 board
                for i in range(0,8):
                        print("-"* 32)
                        print(chr(i+97), end="|")
                        for j in range(0,8):
                                item = self.gameboard.get((i,j), " ")
                                print(str(item)+ " |", end = " ")
                        
            
                        print()
                print("-"* 32)


class Piece():
        
        def __init__(self, color,name):
                self.name = name
                self.position = None
                self.Color = color
        
        #def isValid(self,startposition,endposition, color, gameboard):
        def __repr__(self):
                return str(self.name)
        def  __str__(self):
                return str(self.name)
        
        def availableMoves(self,x,y, gameboard): # beucause unique peices will determine what this means
                print("that no movement exists for the base class")
        
        #def adNauseam(self,x,y,gameboard,Color,intervals): # handle reptitive movemnent
        def isInBounds(self,x,y):
            if x >= 0 and x <8 and y >=0 and y <8:
                    return True
            return False

class Pawn(Piece):
        
        def __init__ (self,Color,name ,direction):
                self.name = name
                self.color = Color
                self.direction = direction
        
        def availableMoves(self, x, y, gameboard,Color = None):
                
                if Color is None:
                        Color = self.Color
                
                answers = []
                if (x+1, y+self.direction) in gameboard and self.noConflict(gameboard,Color,x+1,y+self.direction):
                        answers.append((x+1,y+self.direction))
                
                if(x-1,y + self.direction) in gameboard and self.noConflict(gameboard,Color,x-1,y+self.direction):
                        answers.append((x-1,y+self.direction))
                
                if (x , y + self.direction) not in gameboard and Color == self.color:
                        answers.append((x,y+self.direction))
                
                return answers
unidict = {WHITE:{Pawn: "♙"},BLACK:{Pawn: "♟︎"} }
"""
black
♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜
    
"""
"""
White
    
♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖
"""
                
                
Game().printBoard()