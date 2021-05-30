"""Random Knight Tour:Unlike the standard Knight Tour,this is just moves from one squares to another 
randomly to generate a plot.""" 
import random
import matplotlib.pyplot as plt 
class ChessBoard:
    """ [Base class for Random Knight Tour]"""
    def __init__(self,side:int)->None:
        """ [Constructor to initialize variables] """
        self._side=side
        self._chessboard=[[0 for col in range(self._side)] for row in range(self._side)]
        
    def possibleMovements(self,numIterations:int=50)->list[tuple]:
        """ [Return list positions covered by the knight] """
        x=random.randint(0,self._side-1); y=random.randint(0,self._side-1)
        possible_positions=[]
        positionsCovered=[(x,y)]
        for _ in range(numIterations):
            if x+2<self._side and y+1<self._side:
                possible_positions.append((x+2,y+1))
            
            if x+2<self._side and y-1<self._side and y-1>0:
                possible_positions.append((x+2,y-1))
            
            if x-2<self._side and y+1<self._side and x-2>0:
                possible_positions.append((x-2,y+1))
            
            if x-2<self._side and y-1<self._side and x-2>0 and y-1>0:
                possible_positions.append((x-2,y-1)) 

            if x+1<self._side and y+2<self._side:
                possible_positions.append((x+1,y+2))
            
            if x+1<self._side and y-2<self._side and y-1>0:
                possible_positions.append((x+1,y-2))

            if x-1<self._side and y+2<self._side and x-1>0:
                possible_positions.append((x-1,y+2))
            
            if x-1<self._side and y-2<self._side and x-1>0 and y-2>0:
                possible_positions.append((x-1,y-2))

            newX,newY=random.choice(possible_positions)   #choose randomly among the possible positions,and then repeat this 
            x,y=newX,newY
            positionsCovered.append((newX,newY))                    

        return positionsCovered    
    
    @staticmethod    
    def plotResults(positionsCoverd:list,colorCoordinates:str="blue",colorLine:str="black",linePattern:str="bo")->None:
        xCoors,yCoors=[x for x,y in positionsCoverd],[y for x,y in positionsCoverd]
        plt.title("Plot of positions in Random Knight Tour")
        plt.plot(xCoors,yCoors,"--",color=colorCoordinates)
        for i,j in positionsCoverd:
            plt.plot(i,j,linePattern,color=colorLine)    
        plt.show()    

#Object Instantiation.
chess=ChessBoard(8)
poss_moves=chess.possibleMovements()
chess.plotResults(poss_moves)
