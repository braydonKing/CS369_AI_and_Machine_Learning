from tictactoe import *

def test_finds_successor():
    assert successor(INITIAL_STATE, 0, 'X') == 'X........'


def test_finds_legal_moves():
    assert legal_moves('.X...0...') == [0,2,3,4,6,7,8]