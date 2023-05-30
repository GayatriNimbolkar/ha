#Backtracking

def is_safe(board, row, col, n):
     # Check for row and column
     for i in range(n):
         if board[row][i] == 1 or board[i][col] == 1:
           return False
 
 # Check for upper diagonal
     for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
         if board[i][j] == 1:
           return False
 
 # Check for lower diagonal
     for i,j in zip(range(row,n,1), range(col,-1,-1)):
         if board[i][j] == 1:
            return False
     return True
def solve_n_queens(board, col, n):
    if col >= n:
     return True
 
    for i in range(n):
        if is_safe(board, i, col, n):
         board[i][col] = 1
 
         if solve_n_queens(board, col+1, n):
           return True
 
         board[i][col] = 0
 
    return False
def n_queens(n):
 board = [[0 for _ in range(n)] for _ in range(n)]
 
 if solve_n_queens(board, 0, n) == False:
    print(f"No solution exists for n = {n}")
    return
 
 for i in range(n):
     for j in range(n):
        print(board[i][j], end=" ")
     print()
n = int(input("Enter a Number: "))
n_queens(n)