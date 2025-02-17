
"""
Author: <Braydon King>

Create board state with n queens such that no queen is attacking another.
"""

def slope(x1,y1,x2,y2):
    if x2-x1 == 0:
        return 0
    else:
        result = (y2 - y1)/(x2 - x1)
        return result

def conflicts_diagonal(Qrow,Qcol,solution):
    #x values = row
    #y values = col
    for i in range(len(solution)):
        m = slope(Qrow,Qcol,i,solution[i])
        if m == 1 or m==-1:
            return True
    return False

def conflicts_vertical(queen,solution):
    #if sol in list, return True
    if queen in solution:
        return True
    else:
        return False


def queen_conflict(row,col,solution):
    if conflicts_vertical(col,solution) or conflicts_diagonal(row,col,solution):
        return True
    else:
        return False

def nqueens(num_queens):
    solution = []
    if 1 < num_queens < 4: #no solution
        return solution

    def add_queen(row):
        if row == num_queens:  # Base case, all queens have been placed
            return solution

        for col in range(num_queens): #For each col on the board
            if not queen_conflict(row,col,solution):#Verify legality of move
                solution.append(col)
                result = add_queen(row+1)
                if result: #If adding a queen to the next row completes the problem, return the solution.
                    return result
                solution.pop() #Backtrack, remove a queen instead of making a copy.
    return add_queen(0) #start at row zero
