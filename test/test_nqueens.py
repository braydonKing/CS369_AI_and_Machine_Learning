from nqueens import *


def solves(solver, n):
    """
    Returns true if the function solver, when passed the number n, returns a legal solution to the n-queens puzzle.
    A legal solution should be an iterable (e.g., a list or tuple) of the integers 0 through n - 1. Each indicates
    the row of the queen in that column. A solution is legal if n queens are placed such that no two are on the same
    row, column, or diagonal.
    """
    solution = solver(n)
    if len(solution) != n:
        return False  # Solution wrong length
    if sorted(list(solution)) != list(range(n)):
        return False  # Solution doesn't contain each number exactly once
    for i in range(n):
        for j in range(i + 1, n):
            if solution[i] == solution[j]:
                return False  # Two queens in same row
            if abs(solution[i] - solution[j]) == j - i:
                return False  # Two queens on same diagonal
    return True


def test_3_queens():
    assert not nqueens(3)  # There is no solution

def test__vertical_attack():
    sol = [0,1,2]
    assert conflicts_vertical(0,sol) == True #finds 1 in the solution list therefore returns True

def test_diagonal_does_conflict():
    sol = [0,4,2]
    assert conflicts_diagonal(0,0,sol) == True

def test_diagonal_does_not_conflict():
    sol=[0,2,4]
    assert conflicts_diagonal(0,0,sol) == False


def test_finds_completion_after_one_move():
    """
    For a 5x5 grid, 5 queens:

    o o o X o
    o X o o o
    o o o o X
    o o X o o
    X o o o o
    answer = [0,2,4,1,3]

    *values of indicies = col
    *array index = row

    methods:

    check_diagonal(): check if queen is attacking another diagonally.
    check_vertical(): check if queen is attacking vertically.

    *do not need check_horizontal() here because we are recursively going through the list of values.*

    add_queen(): add a queen to board the at specified row,col.


    """
    assert nqueens(nqueens(5)) == [0,2,4,1,3]

def test_5_queens():
    assert solves(nqueens, 5)


def test_8_queens():
    assert solves(nqueens, 8)

def test_20_queens():
    assert solves(nqueens, 20)
