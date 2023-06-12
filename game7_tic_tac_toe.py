# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:19:13 2023

@author: gshik
"""

import numpy as np
board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s,p2s='x','o'

def place(sym):
    print(np.matrix(board))
    while True:
        row=int(input("Enter the row - (1 , 2 or 3) : "))
        col=int(input("Enter the column - (1 , 2 or 3) : "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Enter the valid place ")
    board[row-1][col-1]=sym
    

def row_check(sym):
    for i in range(3):
        count=0
        for j in range(3):
            if board[i][j]==sym:
                count+=1
        if count==3:
            return True
    return False
    
def col_check(sym):
    for i in range(3):
        count=0
        for j in range(3):
            if board[j][i]==sym:
                count+=1
        if count==3:
            return True
    return False
    
def dia_check(sym):
    count=0
    for i in range(3):
        if board[i][i]==sym:
            count+=1
    if count==3:
        return True
    count=0
    for i in range(3):
        if board[i][-i-1]==sym:
            count+=1
    if count==3:
        return True
    return False
    
def won(sym):
    return row_check(sym) or col_check(sym) or dia_check(sym)
                
    
def play():
    for turn in range(9):
        if turn%2==0:
            print('x\'s turn : ')
            place(p1s)
            if won(p1s):
                print(p1s,' Wins !!') 
                break
        else:
            print('o\'s turn')
            place(p2s)
            if won(p2s):
                print(p2s,' Wins !!') 
                break
    if not(won(p1s)) and not(won(p2s)):
        print('Draw')
        
print("Lets start the game ")
play()
