"""
# the reason why I was getting an error was because I had a smaller case self.Color
in the pawn class in the third if statement 
and I just couldnt figbure it out.
error number two was a conditional logic flow error.
in the main function i had a try and except clause checking if a peice exists
on the board, which should have been its own singular check.
the problem was that i indented everyhithing inside of the
try clause leading to errors. it should have been ON THE SAME SCOPE
which has now been corrected
"""
BLACK = "black"
WHITE = "white"
class Game():
        def __init__(self):
                self.playersturn= BLACK
                self.message= ""
                self.gameboard={}
                self.placePiece()
                self.main()
        
        def placePiece(self):
                for i in range(0,8):
                        self.gameboard[(i,1)] = Pawn(WHITE,unidict[WHITE][Pawn],1)
                        self.gameboard[(i,6)] = Pawn(BLACK,unidict[BLACK][Pawn],-1)
        def main(self):
                while True:
                    self.printBoard()
                    print(self.message)
                    self.message = ""
                    startpos,endpos = self.parseInput()
                    try:
                        target = self.gameboard[startpos]
                    except:
                        self.message = "could not find piece; index probably out of range"
                        target = None
                
                    if target:
                        print("found "+str(target))
                        if target.Color != self.playersturn:
                            self.message = "you aren't allowed to move that piece this turn"
                            continue
                        if target.isValid(startpos,endpos,target.Color,self.gameboard):
                            self.message = "that is a valid move"
                            self.gameboard[endpos] = self.gameboard[startpos]
                            del self.gameboard[startpos]
                            #self.isCheck()
                            if self.playersturn == BLACK:
                                self.playersturn = WHITE
                            else : self.playersturn = BLACK
                        else : 
                            self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                            print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                    else : self.message = "there is no piece in that space"
                
                    
                
                    
        def parseInput(self):
            try:
                a,b = input().split()
                a = (( ord(a[0])-97 ), int(a[1])-1 )
                b = ( (ord(b[0]) -97), int(b[1])-1 )
                print(a,b)
            
                return (a,b)
            except:
                print("error decoding input try again")
                return ((-1,-1),(-1,-1))
        print("please enter an viable algebaric expression separated by a space for example: e7 e6")
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
        
        def isValid(self,startposition,endposition, color, gameboard):
            if endposition in self.availableMoves(startposition[0],startposition[1],gameboard,Color =color):
                   return True
            return False
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
        
        def __init__ (self,color,name ,direction):
                self.name = name
                self.Color = color
                self.direction = direction
        
        def availableMoves(self, x, y, gameboard,Color = None):
                
                if Color is None:
                        Color = self.Color
                
                answers = []
                if (x+1, y+self.direction) in gameboard and self.noConflict(gameboard,Color,x+1,y+self.direction):
                        answers.append((x+1,y+self.direction))
                
                if(x-1,y + self.direction) in gameboard and self.noConflict(gameboard,Color,x-1,y+self.direction):
                        answers.append((x-1,y+self.direction))
                
                if (x , y + self.direction) not in gameboard and Color == self.Color:
                        answers.append((x,y+self.direction))
                
                return answers
unidict = {WHITE:{Pawn: "♙"},BLACK:{Pawn: "♟︎"} }