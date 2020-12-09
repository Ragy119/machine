from IPython.display import clear_output
import random

def display_board(board):
    print (board[0],'|',board[1],'|',board[2])
    print('---------')
    print (board[3],'|',board[4],'|',board[5])
    print('---------')
    print (board[6],'|',board[7],'|',board[8])
    
def player_input():
        
    while(1):
        marker = input("please enter the marker")
        position = int(input("please enter the position"))
        
        if(marker.upper() != 'O' and marker.upper() != 'X'):
            print("Wrong marker")
        else:
            return marker.upper(),position-1
        
def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    flag = 0
  
    if board[0] == mark:
        if   board[1] == mark and board[2] == mark:
            flag = 1
        elif board[3] == mark and board[6] == mark:
            flag = 1
        elif board[4] == mark and board[8] == mark:
            flag = 1
    if board[8] == mark:
        if   board[5] == mark and board[2] == mark:
            flag = 1
        elif board[7] == mark and board[6] == mark:
            flag = 1
    if board[4] == mark:
        if   board[3] == mark and board[5] == mark:
            flag = 1
        elif board[1] == mark and board[7] == mark:
            flag = 1
        elif board[2] == mark and board[6] == mark:
            flag = 1
    
    if flag == 1:
        print("Player {} won the game!".format(mark))
        return flag
        



def choose_first():
    no = random.randint(0,1)
    return no



def space_check(board, position):
        if board[position] == ' ':
            return True
        else:
            return False
        

def full_board_check(board):
    counter = 0
    for i in range(9):
        if board[i] != ' ':
            counter += 1
    
    if counter == 9:
        return True
    else:
        #print(counter)
        return False

    
    
def player_choice(board):
    pos = int(input("Please enter your next position"))
    state = space_check(board, pos)
    if state == True:
        return pos
    
def replay():
    
    ans = input("Do you want to play again? ")
    if ans == 'yes':
        return True
    else:
        return False
    
    
print('Welcome to Tic Tac Toe!')
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

game_on = True


while True:
    # Set the game up here
    pl_st = choose_first()
    if pl_st == 0:
        print("Player 1 will start")
    else: 
        print("Player 2 will start")
    
    
    while game_on:
        #Player 1 Turn
        if (pl_st != 1):
            pl_st = 2
            ch_sp = False
            print("Player 1 turn with X")
            while not ch_sp:
                ma,po = player_input()
                ch_sp = space_check(board,po)
                if ch_sp == True:
                    break
                else:
                    print("wrong position")

            place_marker(board, ma, po)
            display_board(board)
            w1 = win_check(board,'X')
            if w1 == 1:
                print("player 1 won the game")
                break

        #check if full 
        full_st = full_board_check(board)
        if full_st == True:
            print("No one won :(")
            break
        
        # Player2's turn.
        if (pl_st != 0):
            pl_st = 2
            ch_sp = False 
            print("Player 2 turn with O")

            while not ch_sp:
                ma,po = player_input()
                ch_sp = space_check(board,po)
                if ch_sp == True:
                    break
                else:
                    print("wrong position")        

            place_marker(board, ma, po)    
            display_board(board)
            w2 = win_check(board,'O')
            if w2 == 1:
                print("player 2 won the game")
                break
        
        #check if full 
        full_st = full_board_check(board)
        if full_st == True:
            print("No one won :(")
            break
            
            
    #if not replay():
    st_rep = replay()
    if st_rep == False:
        break
   