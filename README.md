# Tic Tac Toe Game

```bash
dadsa dasdadasd
```

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

```python

```

```python

```
Tic Tac  Toe game


- item 1
- item 2

Text teasda das da daskjdand  adka dlak dlak dlakd al
