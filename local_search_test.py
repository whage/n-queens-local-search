from local_search import Queen, attacks, get_num_of_attacking_queens, is_queen

def test_attacks():
    q1 = Queen(3,6)
    q2 = Queen(5,6)
    q3 = Queen(4,4)
    q4 = Queen(2,3)
    q5 = Queen(6,3)
    q6 = Queen(1,2)

    assert attacks(q1, q2)
    assert attacks(q4, q5)
    assert attacks(q1, q5)
    assert attacks(q2, q6)
    assert not attacks(q5, q2)
    assert not attacks(q3, q2)
    assert not attacks(q3, q1)
    assert not attacks(q1, q6)

def test_get_num_of_attacking_queens_1():
    board = [
        Queen(3,6),
        Queen(5,6),
        Queen(4,4),
        Queen(2,3),
        Queen(6,3),
        Queen(1,2),
    ]

    assert get_num_of_attacking_queens(board) == 6

def test_get_num_of_attacking_queens_2():
    board = [
        Queen(1,4),
        Queen(2,4),
        Queen(3,3),
        Queen(4,2),
        Queen(5,5),
        Queen(6,4),
    ]

    assert get_num_of_attacking_queens(board) == 9

def test_is_queen():
    board = [
        Queen(1,4),
        Queen(2,4),
        Queen(3,3),
        Queen(4,2),
        Queen(5,5),
        Queen(6,4),
    ]

    assert True == is_queen(board, 1, 4)
    assert True == is_queen(board, 2, 4)
    assert True == is_queen(board, 3, 3)
    assert True == is_queen(board, 4, 2)
    assert True == is_queen(board, 5, 5)
    assert True == is_queen(board, 6, 4)

    assert False == is_queen(board, 6, 5)
    assert False == is_queen(board, 6, 6)
    assert False == is_queen(board, 6, 3)
