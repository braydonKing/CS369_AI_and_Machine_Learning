
"""
Author: <Braydon King>

Create board state with n queens such that no queen is attacking another.
"""
solution = []

def check_diagonal(queen):
    pass

def check_vertical(queen):
    #if sol in list, return True
    if solution.contains(queen):
        return True
    else:
        return False


def add_queen(col):
    if check_col(col):
        pass
    else:
        check_diagonal(col)
        check_horizontal(col)
        check_vertical(col)

def nqueens(num_queens):
    if 1 < num_queens < 3: #no solution
        return solution

    if len(solution) == num_queens:#base case, all queens have been placed
        return solution
    else:
        #
        pass
