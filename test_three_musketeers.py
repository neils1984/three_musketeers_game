import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 = [ [_, _, _, R, _],
            [_, _, R, _, _],
            [M, R, M, R, M],
            [R, _, _, _, _],
            [_, _, _, R, _] ]

board3 = [ [R, _, _, R, _],
            [_, R, _, R, _],
            [M, _, M, _, _],
            [_, R, _, _, M],
            [_, _, R, R, _] ]

board4 = [ [_, _, _, _, _],
            [_, _, _, _, _],
            [M, _, _, _, _],
            [R, M, _, _, _],
            [M, _, _, _, _] ]

board5 = [ [_, R, _, _, _],
            [_, _, R, _, _],
            [M, R, R, _, _],
            [M, _, _, _, _],
            [M, R, _, _, _] ]

board6 = [ [_, R, _, R, _],
            [_, R, _, R, _],
            [M, _, M, _, _],
            [_, R, _, _, M],
            [_, _, R, R, _] ] #is the same as board 3 after make_move((0,0),right)

board7 = [ [R, _, _, R, _],
            [_, _, M, R, _],
            [M, _, _, _, _],
            [_, R, _, R, M],
            [_, _, R, _, _] ] #is the same as board 3 after make_move((4,3,up)), ((1,1),right), ((2,2),up)

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((2,2)) == M
    assert at((4,4)) == R
    assert at((2,4)) == R
    assert at((1,1)) == R

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    

    set_board(board2)
    assert at((2,0)) == M
    assert at((2,2)) == M
    assert at((2,4)) == M
    assert at((2,1)) == R
    assert at((3,1)) == _

def test_get_board():
    set_board(board1)
    assert board1 == get_board()

    set_board(board2)
    assert board2 == get_board()

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)

    with pytest.raises(ValueError):
        string_to_location('B9')
    assert string_to_location('C3') == (2,2)
    
    with pytest.raises(ValueError):
        string_to_location('AA1')

    assert string_to_location('E5') == (4,4)

def test_location_to_string():
    assert location_to_string((0,0)) == 'A1'

    with pytest.raises(ValueError):
        location_to_string((5,4))

    with pytest.raises(ValueError):
        location_to_string((1,5))

    with pytest.raises(ValueError):
        location_to_string((-1,0))

    with pytest.raises(ValueError):
        location_to_string((0,-1))
        
    assert location_to_string((4,4)) =='E5'
    assert location_to_string((1,1)) == 'B2'
    assert location_to_string((2,3)) == 'C4'
    assert location_to_string((3,0)) == 'D1'
    
def test_at():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((2,3)) == R

    set_board(board1)
    assert at((0,0)) == _
    assert at((3,1)) == R
    assert at((2,2)) == M

    set_board(board2)
    assert at((2,0)) == M
    assert at((3,4)) == _
    assert at((4,4)) == _

def test_all_locations():
    assert all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2),
                             (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0),
                             (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    assert (3,4) in all_locations()
    assert (5,5) not in all_locations()
    assert(-1,0) not in all_locations()
    assert(0,-1) not in all_locations()
               
def test_adjacent_location():
    assert adjacent_location((0,0),right) == (0,1)
    assert adjacent_location((4,0),right) == (4,1)
    assert adjacent_location((4,4),up) == (3,4)
    assert adjacent_location((2,2),down) == (3,2)
    assert adjacent_location((3,2),left) == (3,1)
    assert adjacent_location((0,0),left) == (0,-1)
                   
def test_is_legal_move_by_musketeer():
    create_board()
    assert is_legal_move_by_musketeer((0,4),left) == True

    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,3),down)

    set_board(board1)
    assert is_legal_move_by_musketeer((0,3),right) == False
    assert is_legal_move_by_musketeer((2,2),down) == False
    assert is_legal_move_by_musketeer((2,2),left) == True

    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((1,1),right)
    
    # add more tests here
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((2,1),up) == True
    assert is_legal_move_by_enemy((2,1),right) == False
    assert is_legal_move_by_enemy((4,3),left) == True

    with pytest.raises(ValueError):
        is_legal_move_by_enemy((2,2),left)

    with pytest.raises(ValueError):
        is_legal_move_by_enemy((1,1),left)
        
    # add more tests here
               
def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((2,1),up) == True
    assert is_legal_move((1,3),down) == True
    assert is_legal_move((0,3),down) == False
    assert is_legal_move((2,3),left) == False
    

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((2,1)) == True
    assert can_move_piece_at((0,0)) == False

    create_board()
    assert can_move_piece_at((0,3)) == False

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True

    set_board(board2)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True

    set_board(board3)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True

    set_board(board4)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False
    
def test_possible_moves_from():
    create_board()
    assert possible_moves_from((0,4)) == [left, down]

    set_board(board1)
    assert possible_moves_from((2,2)) == [left, right, up]

    set_board(board2)
    assert possible_moves_from((3,0)) == [right, down]

    set_board(board4)
    assert possible_moves_from((3,0)) == []

def test_is_legal_location():
    assert is_legal_location((0,5)) == False
    assert is_legal_location((-1, 4)) == False
    assert is_legal_location((4, 4)) == True
    assert is_legal_location((0, 0)) == True
    
def test_is_within_board():
    assert is_within_board((4,4),right) == False
    assert is_within_board((0,3),right) == True
    assert is_within_board((4,4),down) == False
    assert is_within_board((0,4),down) == True
    assert is_within_board((0,0),left) == False
    assert is_within_board((0,4),left) == True
    assert is_within_board((0,4),up) == False
    assert is_within_board((1,4),up) == True

def test_all_possible_moves_for():
    
    set_board(board1)
    assert all_possible_moves_for(M) == [((1,3),left),((1,3),down),((2,2),left),((2,2),right),((2,2),up)]
    assert ((1,2),up) in all_possible_moves_for(R)
    assert ((4,3),up) in all_possible_moves_for(R)
    assert ((4,3),right) in all_possible_moves_for(R)

    set_board(board4)
    assert all_possible_moves_for(R) == []
    assert all_possible_moves_for(M) == [((2,0),down),((3,1),left), ((4,0),up)]
    

def test_make_move():
    
    create_board()
    make_move((4,0),up)
    assert at((4,0)) == _
    assert at((3,0)) == M

    set_board(board1)
    make_move((2,2),left)
    assert at((2,2)) == _
    assert at((2,1)) == M
    
    set_board(board3)
    make_move((0,0),right)
    assert at((0,0)) == _
    assert at((0,1)) == R
    assert get_board() == board6

    set_board(board3)
    make_move((4,3),up)
    make_move((1,1),right)
    make_move((2,2),up)
    assert at((4,3)) == _
    assert at((3,3)) == R
    assert get_board() == board7

    
def test_choose_computer_move():
    
    set_board(board1)
    move = choose_computer_move(M)
    assert is_legal_move(move[0], move[1])
    assert is_legal_move_by_musketeer(move[0], move[1])
    move = choose_computer_move(R)
    assert is_legal_move(move[0], move[1])
    assert is_legal_move_by_enemy(move[0], move[1])
    

def test_is_enemy_win():
    create_board()
    assert is_enemy_win() == False

    set_board(board2)
    assert is_enemy_win() == True

    set_board(board5)
    assert is_enemy_win() == True
    
    


