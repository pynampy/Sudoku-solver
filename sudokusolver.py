

board = [[2,0,0,5,0,7,0,0,0],
         [0,0,6,2,3,0,1,0,0],
         [7,5,3,6,0,0,0,4,8],
         [0,0,0,8,0,0,4,5,1],
         [3,0,0,0,6,0,9,0,2],
         [0,8,5,0,2,0,0,3,0],
         [5,0,1,0,0,9,6,0,0],
         [0,4,9,7,0,0,0,0,3],
         [8,2,7,0,0,6,0,9,0]]


        
def solve_sudoku(board):

    if empty(board) == None:
        return True

    else:

        row,col = empty(board)
        print(row,col)

        for i in range(1,10):
            if valid(board,i,row,col):
                board[row][col] = i

                if solve_sudoku(board):
                    return True

                board[row][col] = 0

        return False


def printboard(board):
    for i in range(9):
        if i%3 == 0 and i != 0:
            print("---------------------")
        for j in range(9):
            if j%3 == 0 and j!=0:
                print("|",end=' ')
            print(str(board[i][j]),end=' ')
            if j == 8:
                print('')


def empty(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                return (i,j)
    
    return None


def valid(board,number,x,y):

    for var in range(9): 
        if board[x][var] == number and y != var:
            return False

    for var in range(9):
        if board[var][y] == number  and var != x:
            return False

    box_x = x//3
    box_y = y//3

    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if board[i][j] == number and (i,j) != (x,y):
                return False


    return True

solve_sudoku(board)

printboard(board)








