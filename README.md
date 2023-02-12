# Tic Tac Toe Game

## Description
Tic Tac Toe is a two-player game played on the 3X3 grid between two players. Each player chooses between X and O and the first player starts to draw the X on the space on the grid followed alternatively by the other until a player successfully marks a streak on the grid else if all spaces are filled the game is set to draw.

## Board Design
```python
def board_show():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---|---|---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---|---|---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
```
## Check if is a draw
```python
def check_draw():
    if not ' ' in board:
        return True
    else:
        return False
```

## Check if is a win
```python
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
```

## Game manager
```python
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
```
