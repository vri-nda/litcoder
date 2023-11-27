# Module 1 - Lab 2
import sys

def is_valid_sudoku(board):
    # Checking rows
    for row in board:
        if not is_valid_unit(row):
            return "NO"
    
    
    # Checking columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_unit(column):
            return "NO"
    
    # Checking 3x3 sub-boxes accordingly
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(sub_box):
                return "NO"
    
    return "YES"

def is_valid_unit(unit):
    #accordingly  Checking if each number from 1 to 9 appears exactly once
    seen = set()
    for num in unit:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True

def doSomething(inputVal, size):
    # Converting inputVal to a 2D list representing the Sudoku board accordingly
    board = [list(row.split()) for row in inputVal.strip().split("\n")]
    
    # Checking if the Sudoku board is valid
    outval = is_valid_sudoku(board)
    
    return outval


size = int(input().strip())
inputVal = ""
for _ in range(size):
    row = input().strip()
    inputVal += row + "\n"

outputVal = doSomething(inputVal, size)
print(outputVal)
                                                                                                                            