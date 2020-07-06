# -*- coding: utf-8 -*-

#Strategies to winning on tic-tac-toe
import numpy as np
import random 


def create_board():
    board = np.zeros((3,3),dtype=int)   
    return board


board = create_board()

def place(board, player, position):
   if board[position] == 0:
       board[position] = player
       
   return board
    
def possibilities(board):
    
    return list(zip(*np.where(board == 0)))

possibilities(board)

random.seed(1)
def random_place(board,player):   
    selections = possibilities(board)
    if len(selections) > 0 :
        selection = random.choice(selections)
        place(board, player, selection)     

    return board
        
random.seed(1)

for i in range(3):
    for player in [1,2]:
        random_place(board,player)
    
      
def row_win(board,player):
    if np.any(np.all(board==player,axis=1)):
        return True
    else:
        return False
    
    
def col_win(board,player):
    if np.any(np.all(board==player,axis=0)):
        return True
    else:
        return False
    

def diag_win(board,player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board)==player)):
        return True
    else:
        return False
    
  
def evaluate(board):
    winner = 0
    for player in [1,2]:
        if row_win(board, player) == True:
            winner = player
        elif col_win(board, player) == True:
            winner = player
        elif diag_win(board,player) == True:
            winner = player
        pass
    
    if np.all(board != 0) and winner == 0:
        winner = -1
    
    return winner
    

random.seed(1)


def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break

    return winner

results = [play_game() for i in range(10000)]
print(results.count(1)) #quantidade de vezes que o jogador 1 venceu

random.seed(1)
    
def strategic_play_game():
    board = create_board()
    board[1,1] = 1
    winner = 0
    while winner == 0:
        for player in [2, 1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break

    return winner
    
    
results2 = [strategic_play_game() for i in range(10000)]
print(results2.count(1)) #quantidade de vezes que o jogador 1 venceu   
    
    
    