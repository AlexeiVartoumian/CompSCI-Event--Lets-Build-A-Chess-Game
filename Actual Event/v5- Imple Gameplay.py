BLACK = "black"
WHITE = "white"
"""
1.handle player taking same colour piece
2.handle bishop play, knight play rook play and queen play king play and kinght play
3.place those pieces on the board
"""
#import pdb
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
                
                #step 3
                placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
                for i in range(0,8):
                    self.gameboard[i,0] = placers[i](WHITE,unidict[WHITE][placers[i]])
                    self.gameboard[(7-i),7] = placers[i](BLACK,unidict[BLACK][placers[i]])
                placers.reverse()
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
                a = ((ord(a[0])-97), int(a[1])-1)
                b = (ord(b[0])-97, int(b[1])-1)
                print(a,b)
                return (a,b)
            except:
                print("error decoding input. please try again")
                return((-1,-1),(-1,-1))
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
        
        def isValid(self,startPosition,endPosition,Color,gameboard):
            #pdb.set_trace()
            print(startPosition[0],startPosition[1],"hahaha")
            if endPosition in self.availableMoves(startPosition[0],startPosition[1],gameboard,Color = Color):
                return True
            return False
        def __repr__(self):
                return str(self.name)
        def  __str__(self):
                return str(self.name)
        
        def availableMoves(self,x,y, gameboard): # beucause unique peices will determine what this means
                print("that no movement exists for the base class")
        
        #1 handled here
        def noConflict(self,gameboard,intitialColor,x,y):
              if(self.isInBounds(x,y) and (((x,y) not in gameboard)) or gameboard[(x,y)].Color != intitialColor):
                return True
        #2.handled here refer above
        def AdNauseum(self,x,y,gameboard, Color, intervals): # handle reptitive movement of bishop queen and rook
    
            answers = []
            for xint,yint in intervals:
                xtemp,ytemp = x+xint,y+yint
                while self.isInBounds(xtemp,ytemp):
                    #print(str((xtemp,ytemp))+"is in bounds")
                
                    target = gameboard.get((xtemp,ytemp),None)
                    if target is None: answers.append((xtemp,ytemp))
                    elif target.Color != Color: 
                        answers.append((xtemp,ytemp))
                        break
                    else:
                        break
                
                    xtemp,ytemp = xtemp + xint,ytemp + yint
            return answers
        def isInBounds(self,x,y):# do we repsect the baord
            if x >=0 and x < 8 and y >= 0 and y < 8:
                return True
            return False
        def noConflict(self, gameboard,initialcolour,x,y,): # now we handle a piece colliding with anothe peice of  the same colour need gameboard co-ords and bounds func above
            print("are now this")
            print(x,y)
            # took me an hour to realise why I was getting a 8,8 key error . if forgot a bracket :(
            if(self.isInBounds(x,y) and (((x,y) not in gameboard) or gameboard[(x,y)].Color != initialcolour)):
                return True
            return False
#after doing this we can make the rook ,bishop and queen class and king
chessCardinals = [(1,0),(0,1),(-1,0),(0,-1)]
chessDiagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]
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
class Rook(Piece):
    def availableMoves(self,x,y,gameboard ,Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)
class Bishop(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)
class Queen(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals+chessDiagonals)
def knightList(x,y,int1,int2):
    
    return [(x+int1,y+int2),(x-int1,y+int2),(x+int1,y-int2),(x-int1,y-int2),(x+int2,y+int1),(x-int2,y+int1),(x+int2,y-int1),(x-int2,y-int1)]
def kingList(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]
class King(Piece):
      
      
      def availableMoves(self, x, y, gameboard,Color= None):
            if Color is None: 
                  Color = self.Color
            return [(xx,yy) for xx,yy in kingList(x,y) if self.noConflict(gameboard,Color,xx,yy)]
class Knight(Piece):
    
    
    def availableMoves(self,x,y,gameboard,Color = None):
        if Color is None:
            Color = self.Color
        print(x,y, "still alive")
        return [(xx,yy) for xx,yy in knightList(x,y,2,1) if self.noConflict(gameboard,Color,xx,yy)]
    
      
          
#unidict = {WHITE:{Pawn: "♙"},BLACK:{Pawn: "♟︎"} }
unidict = {WHITE: {Pawn:"♙",Rook:"♖",Knight:"♘",Bishop: "♗",Queen:"♕",King:"♔"},BLACK:{Pawn:"♟︎",Rook:"♜",Knight:"♞",Bishop: "♝",Queen:"♛",King:"♚"}}
     
                
Game()