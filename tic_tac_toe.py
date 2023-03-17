import os,sys
from random import randint as rand
from time import sleep
board=[0,1,2,3,4,5,6,7,8]
turn=0
def display_board():
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    os.system(['clear','cls'][os.name == 'nt'])
    text= '''
          +-------+-------+-------+
          |       |       |       |
          |   {}   |   {}   |   {}   |
          |       |       |       |
          +-------+-------+-------+
          |       |       |       |
          |   {}   |   {}   |   {}   |
          |       |       |       |
          +-------+-------+-------+
          |       |       |       |
          |   {}   |   {}   |   {}   |
          |       |       |       |
          +-------+-------+-------+
          '''
    text=text.format(*board)
    print(text)
def enter_move(move,side):
    board[move]=side

def victory_for():
    winner=None
    if board[0]==board[1] and board[0]==board[2]:winner=board[0]
    elif board[3]==board[4] and board[3]==board[5]:winner=board[3]
    elif board[6]==board[7] and board[6]==board[8]:winner=board[6]
    elif board[0]==board[3] and board[0]==board[6]:winner=board[0]
    elif board[1]==board[4] and board[1]==board[7]:winner=board[1]
    elif board[2]==board[5] and board[2]==board[8]:winner=board[2]
    elif board[0]==board[4] and board[0]==board[8]:winner=board[0]
    elif board[2]==board[4] and board[2]==board[6]:winner=board[2]
    return winner

def draw_move():
    global turn
    fields=[x for x in board if type(x)==int]
    if turn==0:
        print("X Computers turn.")
        sleep(1)
        move=fields[rand(0,len(fields)-1)]
        turn=1
        print(move)
        board[move]="X"
    else:
        while 1:
            try:
                move=int(input("O your turn to enter a number from the grid. >> "))
                if move in fields:
                    board[move]="O"
                    turn=0
                    break
                else:
                    print("Move "+str(move)+" is taken already.")
            except ValueError:
                print("You have to enter a number from the grid.")
            except:
                print("Well you entered some kind of bad data. Just don't know what!")
while 1:
    win=victory_for()
    if win==None:
        display_board()
        draw_move()
    elif win=="X":
        display_board()
        print("X Computer wins!")
    else:
        display_board()
        print("O You win!")
    if win!=None:
        while 1:
            inp=input("Would you like to retry? Y/N ").lower()
            if inp=="y":
                print("restart")
                sleep(1)
                turn=0
                board=[0,1,2,3,4,5,6,7,8]
                break
            elif inp=="n":
                sys.exit()
    

