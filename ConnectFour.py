import math
import copy
import time

# CONSTANTS:
COLUMNS=7
ROWS=6
HUMANTOKEN="x"
COMPUTERTOKEN="o"

#----------------------------------------------------
# GIVEN:
# RETURNS: An empty connect four board
def getEmptyBoard():
    board = []
    for x in range(ROWS):
##        print "x=",x
        board.append(["."]*COLUMNS)
##        print "board=", board[x]
    return board

# TEST:
##print getEmptyBoard()

#-----------------------------------------------------
# GIVEN: Column number and the board list
# Returns: The deepest row number which is empty
def getDeepestEmptyRowInColumn(n,board):
    for x in range(ROWS):
        if (board[x][n]=="."):
            return x
    return -1 # Column Full
# TEST:
# print getDeepestEmptyRowInColumn(2,getEmptyBoard())

#------------------------------------------------------
# GIVEN: Column number, board list and humans turn or not
# RETURNS: Updated list of board
def insertInColumn(n,boardUpdate,isHuman):
    x = getDeepestEmptyRowInColumn(n,boardUpdate)
    if x == -1:
        return None # Column Full
    if isHuman:
        boardUpdate[x][n]=HUMANTOKEN
    else:
        boardUpdate[x][n]=COMPUTERTOKEN
    return boardUpdate

# TEST:
##print insertInColumn(0,getEmptyBoard(),True)
##print insertInColumn(0,insertInColumn(0,getEmptyBoard(),True),False)

#------------------------------------------------------
# GIVEN: A column number and a board list
# RETURNS: true if its possible put disc in that column else false
def isValidMove(n, board):
    if (n >= COLUMNS or n < 0 or getDeepestEmptyRowInColumn(n,board)==-1):
        return False
    return True
# TEST:
b1= insertInColumn(0,insertInColumn(0,getEmptyBoard(),True),False)
b2= insertInColumn(0,insertInColumn(0,b1,True),False)
b3= insertInColumn(0,insertInColumn(0,b2,True),False)
b4= insertInColumn(2,insertInColumn(1,b3,True),True)
##print b3
##print isValidMove(0,b3)

#------------------------------------------------------
# GIVEN: A board list
# RETURNS: A list of possible moves
def getPossibleMovesColumn(board):
    moves=[]
    for n in range(COLUMNS):
        if isValidMove(n,board):
            moves.append(n)
    return moves
# TEST:
##print getPossibleMovesColumn(b3)

#------------------------------------------------------
# GIVEN: A board list
# RETURNS: Board list to be displayed
def printBoard(board):
##    r=0
##    c=0
    print "         0     1     2     3     4     5     6"
    print "       ----------------------------------------"
    for x in range(ROWS-1,-1,-1):
##        r=r+1
        print "%d ) " %x,
        for y in range(0,COLUMNS):
##            c=c+1
##            print " c=",c
            print " | ",board[x][y],
        print "|"
        print "       ----------------------------------------"
##        print "r=",r
##        print "_____________"
# TEST:
##print printBoard(b3)
##print printBoard(getEmptyBoard())
##printBoard(insertInColumn(1,getEmptyBoard(),True))

#-----------------------------------------------------------

def isWinner(board):
##    print "1"
    for x in range(ROWS): # Checks horizontal tokens
        for y in range(COLUMNS - 3):
            if (board[x][y]==board[x][y+1] and board[x][y+2]==board[x][y] and board[x][y+3]==board[x][y]):
                if (board[x][y]== HUMANTOKEN or board[x][y]==COMPUTERTOKEN):
                    return True
##    print "2"
    for x in range(ROWS - 3): # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y]==board[x+1][y] and board[x+2][y]==board[x][y] and board[x+3][y]==board[x][y]):
                if (board[x][y]== HUMANTOKEN or board[x][y]==COMPUTERTOKEN):
                    return True
##    print "3"                
    for x in range(ROWS - 3): # Checks diagional 1 tokens
        for y in range(COLUMNS - 3):
            if (board[x][y]==board[x+1][y+1] and board[x+2][y+2]==board[x][y] and board[x+3][y+3]==board[x][y]):
                if (board[x][y]== HUMANTOKEN or board[x][y]==COMPUTERTOKEN):
                    return True
##    print "4"
    for x in range(ROWS-3): # Checks diagional 2 tokens
        for y in range(3, COLUMNS):
            if (board[x][y]==board[x+1][y-1] and board[x+2][y-2]==board[x][y] and board[x+3][y-3]==board[x][y]):
                if (board[x][y]== HUMANTOKEN or board[x][y]==COMPUTERTOKEN):
                    return True
    return False
##print printBoard(b4)
##print isWinner(b4)
##print getPossibleMovesColumn(b4)

## ---For Horizontal
##insertInColumn(3,b4,True)
##print printBoard(b4)
##print isWinner(b4)

## ---For vertical
##insertInColumn(3,b4,False)
##insertInColumn(3,b4,False)
##insertInColumn(3,b4,False)
##print printBoard(b4)
##print isWinner(b4)

## --- For Diagonal 1
##insertInColumn(1,b4,True)
##insertInColumn(2,b4,False)
##insertInColumn(2,b4,True)
##insertInColumn(3,b4,False)
##insertInColumn(3,b4,False)
##insertInColumn(3,b4,False)
##insertInColumn(3,b4,True)
##print printBoard(b4)
##print isWinner(b4)

## --- For Diagonal 2
##insertInColumn(2,b4,False)
##insertInColumn(1,b4,False)
##insertInColumn(1,b4,False)
##insertInColumn(3,b4,False)
##print printBoard(b4)
##print isWinner(b4)

#---------------------------------------------------------------

def minimax(board,depth,isHuman):
##    if depth==0 or len(getPossibleMovesColumn(board))==0:
##        return (0, random.choice(getPossibleMovesColumn(board)))
    if isHuman:
        print "Human"
    else:
        possibleMoves=getPossibleMovesColumn(board)
        bestValue = -99999
        bestMove = possibleMoves[0]
##        sumOfValues=0
        count=0
##        subs=0
        for x in possibleMoves:
            tempBoard=copy.deepcopy(board)
            insertInColumn(x,tempBoard,isHuman)
##            print "move in minimax",x
            v = minimizer(tempBoard,depth)
##            sumOfValues = sumOfValues + v
##            if (len(possibleMoves)%2==0):
##                if (count>=(len(possibleMoves)/2)):
##                    subs+=1
##                v += count-((2*subs)+1)
##            else:
##                if (count>(len(possibleMoves)/2)):
##                    subs+=1
##                v += count-((2*subs))
            v+=3-math.fabs(3-x)
##            print "x=",x,
##            print " v=",v
            if bestValue < v:
                bestValue = v
                bestMove = x
##            print "bestValue=",bestValue
            count+=1
        return bestMove

def minimizer(board,depth):
    possibleMoves=getPossibleMovesColumn(board)
    if depth==0 or len(possibleMoves)==0 or isWinner(board):
##        score=evaluationFunction(board,True)-evaluationFunction(board,False)
        score=evaluationFunction(board,False)-evaluationFunction(board,True)
##        score=evaluationFunction(board,True)
##        print "mini=",score
        return score
    bestValue= 99999
    for x in possibleMoves:
        tempBoard=copy.deepcopy(board)
        insertInColumn(x,tempBoard,True)
##        print "move taken by human=",x,
        v = maximizer(tempBoard,depth-1)
##        print "v=",v
        if bestValue > v:
            bestValue = v
##    print "mini bestValue=",bestValue
    return bestValue

def maximizer(board,depth):
    possibleMoves=getPossibleMovesColumn(board)
    if depth==0 or len(possibleMoves)==0 or isWinner(board):
        score=evaluationFunction(board,False)-evaluationFunction(board,True)
##        score=evaluationFunction(board,False)
##        print "maxi=",score
        return score
    bestValue= -99999
    for x in possibleMoves:
        tempBoard=copy.deepcopy(board)
        insertInColumn(x,tempBoard,False)
##        print "move taken by comp=",x,
        v = minimizer(tempBoard,depth)
##        print "v=",v
        if bestValue < v:
            bestValue = v
##    print "maxi bestValue", bestValue
    return bestValue
#---------------------------------------------------------------

def negaMax(board,depth,isHuman):
##    if depth==0 or len(getPossibleMovesColumn(board))==0:
##        return (0, random.choice(getPossibleMovesColumn(board)))
    if isHuman:
        print "Human"
    else:
        possibleMoves=getPossibleMovesColumn(board)
        bestValue = -99999
        bestMove = possibleMoves[0]
##        sumOfValues=0
        count=0
##        subs=0
        for x in possibleMoves:
            tempBoard=copy.deepcopy(board)
            insertInColumn(x,tempBoard,isHuman)
##            print "move in minimax",x
            v = -negamizer(tempBoard,depth,-1)
##            sumOfValues = sumOfValues + v
##            if (len(possibleMoves)%2==0):
##                if (count>=(len(possibleMoves)/2)):
##                    subs+=1
##                v += count-((2*subs)+1)
##            else:
##                if (count>(len(possibleMoves)/2)):
##                    subs+=1
##                v += count-((2*subs))
            v+=3-math.fabs(3-x)
##            print "x=",x,
##            print " v=",v
            if bestValue < v:
                bestValue = v
                bestMove = x
##            print "bestValue=",bestValue
            count+=1
        return bestMove

##def negamizer(board,depth,turn):
##    possibleMoves=getPossibleMovesColumn(board)
##    if depth==0 or len(possibleMoves)==0 or isWinner(board):
####        score=evaluationFunction(board,True)-evaluationFunction(board,False)
##        score=evaluationFunction(board,False)-evaluationFunction(board,True)
####        score=evaluationFunction(board,True)
####        print "mini=",score
##        return turn*score
##    bestValue= 99999
##    for x in possibleMoves:
##        tempBoard=copy.deepcopy(board)
##        insertInColumn(x,tempBoard,True)
####        print "move taken by human=",x
##        v = maximizer(tempBoard,depth-1)
##        if bestValue > v:
##            bestValue = v
####    print "mini bestValue=",bestValue
##    return bestValue

def negamizer(board,depth,turn):
    possibleMoves=getPossibleMovesColumn(board)
    if depth==0 or len(possibleMoves)==0 or isWinner(board):
        score=evaluationFunction(board,False)-evaluationFunction(board,True)
##        score=evaluationFunction(board,False)
##        print "maxi=",score
        return turn*score
##        return turn*score
    bestValue= -99999
    for x in possibleMoves:
        tempBoard=copy.deepcopy(board)
        insertInColumn(x,tempBoard,turn==-1)
##        print "move taken by ",turn ,"=",x,
##        v = -1 * negamizer(tempBoard,depth-1,-1*turn)
        if turn==1:
            v = -negamizer(tempBoard,depth,-1*turn)
        else:
            v = -negamizer(tempBoard,depth-1,-1*turn)
##        print " v=",v
        if bestValue < v:
            bestValue = v
##    print "maxi bestValue", bestValue
    return bestValue

#---------------------------------------------------------------

def alphaBetaPruning(board,depth,isHuman):
##    if depth==0 or len(getPossibleMovesColumn(board))==0:
##        return (0, random.choice(getPossibleMovesColumn(board)))
    if isHuman:
        print "Human"
    else:
        possibleMoves=getPossibleMovesColumn(board)
        bestValue = -99999
        actualBestValue=-99999
        a=-99999
        b=99999
        bestMove = possibleMoves[0]
##        sumOfValues=0
        count=0
##        subs=0
        for x in possibleMoves:
            tempBoard=copy.deepcopy(board)
            insertInColumn(x,tempBoard,isHuman)
##            print "move in minimax",x
            v = abminimizer(tempBoard,depth,a,b)
##            sumOfValues = sumOfValues + v
##            if (len(possibleMoves)%2==0):
##                if (count>=(len(possibleMoves)/2)):
##                    subs+=1
##                v += count-((2*subs)+1)
##            else:
##                if (count>(len(possibleMoves)/2)):
##                    subs+=1
##                v += count-((2*subs))
##            v=v+3-math.fabs(3-x)
            modifiedV=v+3-math.fabs(3-x)
##            print "x=",x,
##            print " v=",v
##            if bestValue < v:
##                bestValue = v
##                bestMove = x
            if bestValue < modifiedV:
                bestValue=modifiedV
                bestMove=x
                actualBestValue=v
            if a < actualBestValue:
                a= actualBestValue
            count+=1
##            print "bestValue=",bestValue
            
        return bestMove

def abminimizer(board,depth,a,b):
    possibleMoves=getPossibleMovesColumn(board)
    if depth==0 or len(possibleMoves)==0 or isWinner(board):
##        score=evaluationFunction(board,True)-evaluationFunction(board,False)
        score=evaluationFunction(board,False)-evaluationFunction(board,True)
##        score=evaluationFunction(board,True)
##        print "mini=",score
        return score
    bestValue= 99999
    for x in possibleMoves:
        tempBoard=copy.deepcopy(board)
        insertInColumn(x,tempBoard,True)
##        print "move taken by human=",x
        v = abmaximizer(tempBoard,depth-1,a,b)
        if bestValue > v:
            bestValue = v
        if b > bestValue:
            b= bestValue
##        print "b=",b
        if bestValue<a :
##            print "a=",a
            return bestValue
##    print "mini bestValue=",bestValue
    return bestValue

def abmaximizer(board,depth,a,b):
    possibleMoves=getPossibleMovesColumn(board)
    if depth==0 or len(possibleMoves)==0 or isWinner(board):
        score=evaluationFunction(board,False)-evaluationFunction(board,True)
##        score=evaluationFunction(board,False)
##        print "maxi=",score
        return score
    bestValue= -99999
    for x in possibleMoves:
        tempBoard=copy.deepcopy(board)
        insertInColumn(x,tempBoard,False)
##        print "move taken by comp=",x
        v = abminimizer(tempBoard,depth,a,b)
        if bestValue < v:
            bestValue = v
        if a < bestValue :
            a = bestValue
##        print "a=",a
        if bestValue > b :
##            print "b=",b
            return bestValue
##    print "maxi bestValue", bestValue
    return bestValue

#---------------------------------------------------------------
def fourInARow(board,isHuman):
##    print "1"
    
    if isHuman:
        token=HUMANTOKEN
    else:
        token=COMPUTERTOKEN
    count=0
    for x in range(ROWS): # Checks horizontal tokens
        for y in range(COLUMNS - 3):
            if (board[x][y]==board[x][y+1] and board[x][y+2]==board[x][y] and board[x][y+3]==board[x][y]):
                if (board[x][y]== token):
                    count+=1
##                    return True
##    print "2"
    for x in range(ROWS - 3): # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y]==board[x+1][y] and board[x+2][y]==board[x][y] and board[x+3][y]==board[x][y]):
                if (board[x][y]== token):
                    count+=1
##                    return True
##    print "3"                
    for x in range(ROWS - 3): # Checks diagional 1 tokens
        for y in range(COLUMNS - 3):
            if (board[x][y]==board[x+1][y+1] and board[x+2][y+2]==board[x][y] and board[x+3][y+3]==board[x][y]):
                if (board[x][y]== token):
                    count+=1
##                    return True
##    print "4"
    for x in range(ROWS-3): # Checks diagional 2 tokens
        for y in range(3, COLUMNS):
            if (board[x][y]==board[x+1][y-1] and board[x+2][y-2]==board[x][y] and board[x+3][y-3]==board[x][y]):
                if (board[x][y]== token):
                    count+=1
##                    return True
    return count
#---------------------------------------------------------------
def threeInARow(board,isHuman):
##    print "1"
    
    if isHuman:
        token=HUMANTOKEN
    else:
        token=COMPUTERTOKEN
    count=0
    for x in range(ROWS): # Checks horizontal tokens
        for y in range(COLUMNS - 2):
            if (board[x][y]==board[x][y+1] and board[x][y+2]==board[x][y] ):
                if (board[x][y]== token):
                    if ((y != 0 and board[x][y-1]=='.') or (y!=(COLUMNS-3) and (board[x][y+3]=='.'))):
                        count+=1
##                    return True
##    print "2"
    for x in range(ROWS - 2): # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y]==board[x+1][y] and board[x+2][y]==board[x][y] ):
                if (board[x][y]== token):
                    if (x!=(ROWS-3) and board[x+3][y]=='.'):
                        count+=1
##                    return True
##    print "3"                
    for x in range(ROWS - 2): # Checks diagional 1 tokens
        for y in range(COLUMNS - 2):
            if (board[x][y]==board[x+1][y+1] and board[x+2][y+2]==board[x][y] ):
                if (board[x][y]== token):
                    if (x!=(ROWS-3) and y!=(COLUMNS-3) and board[x+3][y+3]=='.'):
                        count+=1
##                    return True
##    print "4"
    for x in range(ROWS-2): # Checks diagional 2 tokens
        for y in range(2, COLUMNS):
            if (board[x][y]==board[x+1][y-1] and board[x+2][y-2]==board[x][y]):
                if (board[x][y]== token):
                    if(x!=(ROWS-3) and y!=0 and board[x+3][y-3]=='.'):
                        count+=1
##                    return True
    return count

#---------------------------------------------------------------
def threeInARowWithWinPos(board,isHuman):
##    print "1"
    
    if isHuman:
        token=HUMANTOKEN
    else:
        token=COMPUTERTOKEN
    count=0
    for x in range(ROWS): # Checks horizontal tokens
        for y in range(COLUMNS - 2):
            if (board[x][y]==board[x][y+1] and board[x][y+2]==board[x][y] ):
                if (board[x][y]== token):
                    if ((y != 0 and board[x][y-1]=='.') and (y!=(COLUMNS-3) and (board[x][y+3]=='.'))):
                        count+=1
##                    return True
##    print "3"                
    for x in range(ROWS - 2): # Checks diagional 1 tokens
        for y in range(COLUMNS - 2):
            if (board[x][y]==board[x+1][y+1] and board[x+2][y+2]==board[x][y] ):
                if (board[x][y]== token):
                    if (x!=(ROWS-3) and y!=(COLUMNS-3) and board[x+3][y+3]=='.') and (x!=0 and y!=0 and board[x-1][y-1]=='.'):
                        count+=1
##                    return True
##    print "4"
    for x in range(ROWS-2): # Checks diagional 2 tokens
        for y in range(2, COLUMNS):
            if (board[x][y]==board[x+1][y-1] and board[x+2][y-2]==board[x][y]):
                if (board[x][y]== token):
                    if(x!=(ROWS-3) and y!=0 and board[x+3][y-3]=='.')and (x!=0 and y!=(COLUMNS-1) and board[x-1][y+1]=='.'):
                        count+=1
##                    return True
    return count
#---------------------------------------------------------------
def twoInARow(board,isHuman):
##    print "1"
    
    if isHuman:
        token=HUMANTOKEN
    else:
        token=COMPUTERTOKEN
    count=0
    for x in range(ROWS): # Checks horizontal tokens
        for y in range(COLUMNS - 1):
            if (board[x][y]==board[x][y+1]):
                if (board[x][y]== token):
                    if ((y != 0 and board[x][y-1]=='.') or (y!=(COLUMNS-2) and (board[x][y+2]=='.'))):
                        count+=1
##                    return True
##    print "2"
    for x in range(ROWS - 1): # Checks vertical tokens
        for y in range(COLUMNS):
            if (board[x][y]==board[x+1][y]):
                if (board[x][y]== token):
                    if (x!=(ROWS-2) and board[x+2][y]=='.'):
                        count+=1
##                    return True
##    print "3"                
    for x in range(ROWS - 1): # Checks diagional 1 tokens
        for y in range(COLUMNS - 1):
            if (board[x][y]==board[x+1][y+1]):
                if (board[x][y]== token):
                    if (x!=(ROWS-2) and y!=(COLUMNS-2) and board[x+2][y+2]=='.'):
                        count+=1
##                    return True
##    print "4"
    for x in range(ROWS-2): # Checks diagional 2 tokens
        for y in range(1, COLUMNS):
            if (board[x][y]==board[x+1][y-1]):
                if (board[x][y]== token):
                    if(x!=(ROWS-2) and y!=0 and board[x+2][y-2]=='.'):
                        count+=1
##                    return True
    return count

#---------------------------------------------------------------
def evaluationFunction(board, isHuman):
    FourInARow=100000
    ThreeWinPos=1000
    ThreeInARow=100
    TwoInARow=5
##    print "fourInARow",fourInARow(board,isHuman)
##    print "ThreeInARow",threeInARow(board,isHuman)
    return (FourInARow*fourInARow(board,isHuman))+(ThreeWinPos*threeInARowWithWinPos(board,isHuman)) + (ThreeInARow*threeInARow(board,isHuman))+(TwoInARow*twoInARow(board,isHuman))
    
#---------------------------------------------------------------

def getComputerMove(board,depth,algo):
    start_time=time.clock()
    if algo == 1:
        bestMove=minimax(board,depth,False)
    elif algo==2:
        bestMove=negaMax(board,depth,False)
    else:
        bestMove=alphaBetaPruning(board,depth,False)
    print time.clock()-start_time,"seconds to calculate the computer move"
    insertInColumn(bestMove,board,False)

#---------------------------------------------------------------
## Testing:
##print printBoard(b4)
##print threeInARow(b4,True)
## Testing End
#---------------------------------------------------------------
def main():
    print "Welcome to connect four game"
    print "Please choose a difficulty level -> 0:Easy 1:Medium 2:Hard 3:Expert"
    difficulty=int(input())
    print "Difficulty level chosen is ",difficulty
    print "Please choose the algorithm to use -> 1.) MiniMax 2.)NegaMax 3.) Alpha Beta"
    algorithm=int(input())
    print "You have chosen ",algorithm
    print "Choose who plays first -> 1:Human 2:Computer"
    firstPlayer=int(input())
    print "%d player's move"%firstPlayer
    gameBoard=getEmptyBoard()
    if firstPlayer==2:
        getComputerMove(gameBoard,difficulty,algorithm)
    while ((not isWinner(gameBoard)) and (len(getPossibleMovesColumn(gameBoard))>0)):
        print "Human Move:"
        print printBoard(gameBoard)
        print "Choose a column from ",getPossibleMovesColumn(gameBoard)
        enteredColumn= int(input())
        if enteredColumn in getPossibleMovesColumn(gameBoard):
            insertInColumn(enteredColumn,gameBoard,True)
##            insertInColumn(enteredColumn,gameBoard,False)
            print printBoard(gameBoard)
            if not isWinner(gameBoard):
                print "Computer Move"
                getComputerMove(gameBoard,difficulty,algorithm)
        else:
            print "\nPlease choose a valid entry"
    if isWinner(gameBoard):
        if (fourInARow(gameBoard,True)>0):
            print "Human wins!!!"
        else:
            print printBoard(gameBoard)
            print "Computer Wins!!!"
    else:
        print "Game has been drawn"

        
if __name__ == '__main__':
    main()
