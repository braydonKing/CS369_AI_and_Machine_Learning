from tictactoe import *

def test_finds_successor():
    assert successor(INITIAL_STATE, 0, 'X') == 'X........'


def test_finds_legal_moves():
    assert legal_moves('.X...0...') == [0,2,3,4,6,7,8]

def test_finds_win_for_x():
    assert winner('.X..X..X.') == 1

def test_finds_win_for_o():
    assert winner('.O..O..O.') == -1

def test_finds_value_at_end_of_game():
    assert min_value('...XXX.OO') == 1
    assert max_value('...XXX.OO') == 1

def test_finds_win_in_one_move():
    assert max_value('XX....O.O') == 1

def test_finds_value_after_two_moves():
    assert min_value('XOXXXOO..') == 0

def test_finds_value_after_three_moves():
    # assert max_value('.X.X.O.O.') == 1
    assert min_value('.X.X.O.O.') == -1

