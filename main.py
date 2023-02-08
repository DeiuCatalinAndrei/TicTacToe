def board_show():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---|---|---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---|---|---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_draw():
    if not ' ' in board:
        return True
    else:
        return False

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False
    
player = "X"
board = [' '] * 9
gameover = False
board_show()

while not gameover:
    try:
        move = int(input(f'In which box do you want to move player {player} (1-9) '))
        if board[move-1] == ' ':
            board[move-1] = player
            board_show()
            if check_win(board, player):
                gameover = True
                print(f'Player {player} won the game')
                
            if check_draw() and not gameover:
                gameover = True
                print('The game is a draw')
                
            if player == "X":
                player = "0"
            else:
                player = "X"
        else:
            print("This box is occupied")
    except:
        print('The number entered is not correct')
