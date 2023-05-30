def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()
 

def isSafe(row, col, nd, rd,rowLookup, ndLookup,rdLookup):
    if (ndLookup[nd[row][col]] or rdLookup[rd[row][col]] or rowLookup[row]):
        return False
    return True
 

def solveNQueensUtil(board, col, nd, rd,rowLookup, ndLookup,rdLookup):   
    if(col >= N):
        return True
    for i in range(N):
        if(isSafe(i, col, nd, rd,rowLookup, ndLookup,rdLookup)):
                     
           
            board[i][col] = 1
            rowLookup[i] = True
            ndLookup[nd[i][col]] = True
            rdLookup[rd[i][col]] = True
             
           
            if(solveNQueensUtil(board, col + 1,nd, rd,rowLookup, ndLookup,rdLookup)):
                return True            
            board[i][col] = 0
            rowLookup[i] = False
            ndLookup[nd[i][col]] = False
            rdLookup[rd[i][col]] = False    
    return False
 
def solveNQueens(N):
    
    board = [[0 for i in range(N)] for j in range(N)]
     
    
    nd = [[0 for i in range(N)] for j in range(N)]
    rd = [[0 for i in range(N)] for j in range(N)]    
    rowLookup = [False] * N
     
    
    x = 2 * N - 1
    ndLookup = [False] * x
    rdLookup= [False] * x
     

    for r in range(N):
        for c in range(N):
            nd[r][c] = r + c
            rd[r][c] = r - c + N - 1
     
    if(solveNQueensUtil(board, 0, nd, rd,rowLookup, ndLookup,rdLookup) == False):
        print("Solution does not exist")
        return False
         
    
    printSolution(board)
    return True

"""while True:
    N=int(input("Enter a Number: "))
    solveNQueens(N)
    
    ch=(input("Do you want to continue?(y/n): "))
    if ch=='y':
        N=int(input("Enter a Number: "))
        solveNQueens(N)
    else:
        break;"""
        
#Backtracking

"""def is_safe(board, row, col, n):
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
n_queens(n)"""


'''while True :
     print("****MENU****")
     print("1.Backtracking.")
     print("2.Branch n Bound.")
     print("3.Exit.")
     ch=int(input("Enter your choice : "))
     if ch==1 :
        n = int(input("Enter a Number of Queens: "))
        print("Solved by Backtracking .")
        n_queens(n)
     elif ch==2 :
       N=int(input("Enter the number of Queens"))
       print("Solved by Branch n Bound")
       solveNQueens(N)
     else :
       print("Invalid choice")
       break '''
   
'''def is_safe(board,col,row,n):
     for i in range(n):
         if borad[row][i]==1 or borad[i][col]==1:
             return False
     for i,j in zip(range(row,-1,-1),(col,-1,-1)):
        if board[i][j]==1:
            return False
    
     for i,j in zip(range(row,n,-1),(col,-1,-1)):
        if board[i][j]==1:
            return False 
        return True 
        
        
def solve_n_queens(board,col,n):
        if(col>=n):
            return True
        
        for i in range(n):
         if is_safe(board,i,col,n):
            board[i][col]=1
             
        if solve_n_queens(board,col+1,n):
            return True
        board[i][col]=0
        
        return False
def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
        
        
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()
n = int(input("Enter a Number: "))
n_queens(n)'''
            
    
            
            
            
                  
