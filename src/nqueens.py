
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

    if 1 < num_queens < 3: #no solution
        return solution

    if len(solution) == num_queens:#base case, all queens have been placed
        return solution
    else:
       pass

