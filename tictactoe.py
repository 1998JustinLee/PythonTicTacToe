#! python3
import random

#Global variables
win = False
draw = False
play = True
playChoice= True
winPos = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(1,5,9)]
corner = [1,3,7,9]
cornerChoice = 0
corn = False
result = []
move = 0
tempMove = 0
shouldI = False
mark = ['x','o']
markChoice = 0
markH = 0
markA = 0
#Positions of marks
globMove = []
xMove = [] #This should be human
yMove = []
#Whos turn is it
turn = False #False is for humans
#The board
pos = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
board = ''
scoreH = 0
scoreA = 0
valid = False

def drawBoard():
    board = '''
 %s | %s | %s 
-----------
 %s | %s | %s 
-----------
 %s | %s | %s 
''' %(pos[6],pos[7],pos[8],pos[3],pos[4],pos[5],pos[0],pos[1],pos[2])
    print(board)

#appends combination with 2 positions filled to result
def checkFun(hum, ai):
    for i in range(0, int(len(hum))-1): 
        for j in range(i+1, int(len(hum))): #loop through every pair of positions
            for k in range(0,8): #loop through every triple
                if hum[i] in winPos[k] and hum[j] in winPos[k]: #check if there is a double
                    for l in range(0, int(len(ai))):
                        if ai[l] in winPos[k]: #if the other player has placed a mark in the double, break
                            break
                        elif l == int(len(ai))-1 and ai[l] not in winPos[k]: #if not, make it the next move
                            global result
                            global tempMove
                            global shouldI
                            result.insert(0,winPos[k])
                            tempMove = 0
                            tempMove = 3 - winPos[k].index(hum[i]) - winPos[k].index(hum[j])
                            shouldI = True
                                    
#AI for what choice to make
def choiceFun():
    global shouldI
    global result
    global tempMove, corn, move

    checkFun(yMove, xMove) #check if the AI has a double
    attack = tempMove
    attackTemp = result
    result = []
    tempMove = 0

    if shouldI == True:
        move = attackTemp[0][attack] #if AI has a double, place there
    else:
        shouldI = False
        checkFun(xMove, yMove) #check if human has a double
        block = tempMove
        tempMove = 0
        blockTemp = result
        result = []

        if shouldI == True:
            move = blockTemp[0][block] #if human has a double, block it
        elif corner[0] not in globMove or corner[1] not in globMove or corner[2] not in globMove or corner[3] not in globMove: #if there is an available corner
            while corn == False:
                cornerChoice = random.randint(0,3) #randomly choose one
                if corner[cornerChoice] not in globMove:
                    move = corner[cornerChoice]
                    corn = True
        else: #pick a random available space
            for i in range(1,10):
                if i not in globMove:
                    move = i
            
    shouldI = False
    corn = False

#determines if someone has won                        
def winFun(hum, ai):
    for i in range(0, int(len(hum))-2):
        for j in range(i+1, int(len(hum))-1):
            for k in range(j+1, int(len(hum))): #loop through every possible triples
                for l in range(0,8): #loop through all triples
                    if hum[i] in winPos[l] and hum[j] in winPos[l] and hum[k] in winPos[l]: #if there is a triple, then set win = True
                        global win
                        win = True

def moveFun():
    global move, markH, markA
    if turn == False:
        pos[move-1] = markH
    else:
        pos[move-1] = markA

def markCh():
    global markChoice, markH, markA, valid
    print('Choose your mark, x or o')
    while valid == False:
        markChoice = input()
        if markChoice == 'x' or markChoice == 'X' or markChoice == 'o' or markChoice == 'O':
            valid = True
        else:
            print('Invalid')
    valid = False
    if markChoice == 'x' or markChoice == 'X':
        markH = 'x'
        markA = 'o'
    elif markChoice == 'o' or markChoice == 'O':
        markH = 'o'
        markA = 'x'

def turnSelect():
    global turn
    print('Who goes first?')
    whoGoes = random.randint(0,1)
    if whoGoes == 0:
        turn = False
        print('Human Challenger')
    else:
        turn = True
        print('AI')

def drawFun():
    global pos, draw, win
    if int(len(globMove)) == 9:
        win = True
        draw = True

#game
print('Just type in which square you want to place your mark')
pos = ['1','2','3','4','5','6','7','8','9']
drawBoard()
while play == True:
    win = False
    draw = False
    result = []
    move = 0
    tempMove = 0
    shouldI = False
    mark = ['x','o']
    markChoice = 0
    markH = 0
    markA = 0
    #Positions of marks
    globMove = []
    xMove = [] #This should be human
    yMove = []
    #Whos turn is it
    turn = False #False is for humans
    #The board
    pos = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    board = ''
    valid = False

    #game
    print('')
    print('Current Score')
    print('Human: '+str(scoreH))
    print('AI: '+str(scoreA))
    print('')
    markCh()
    turnSelect()
    while win == False:
        #gameplay
        if turn == False: #human turn
            drawBoard()
            valid = False
            
            while valid == False: #make sure choice hasn't been chosen
                move = input()
                try:
                    move = int(move)
                    if move in globMove or move >=10 or move <=0:
                        print('Nu uh')
                    else:
                        valid = True
                except ValueError:
                    print('Nu uh')
                    
            xMove.append(move)
            moveFun()
            turn = True
            winFun(xMove, yMove)
        else:
            choiceFun()        
            yMove.append(move)
            moveFun()
            turn = False
            winFun(yMove, xMove)

        globMove.append(move)
        drawFun()
        block = None
        attack = None
        result = []
        
    drawBoard()
    if draw == True:
        print('Draw')
    elif turn == False:
        print('AI winner')
        scoreA+=1
    elif turn == True:
        print('Human winner')
        scoreH+=1

    valid = False
    print('Do you want to play again? y/n')
    while valid == False:
        playChoice = input()
        if playChoice == 'y' or playChoice == 'Y' or playChoice == 'n' or playChoice == 'N':
            valid = True
        else:
            print('Invalid')
    valid = False
    
    if playChoice == 'y' or playChoice == 'Y':
        play = True
    elif playChoice == 'n' or playChoice == 'N':
        play = False
