from main import start_draw_board, create_board, draw_board, check_win_extracted, check_win

def test__start_draw_board__return_start_board():
    assert start_draw_board() == '1|2|3\n=====\n4|5|6\n=====\n7|8|9\nВыше изображена игральная доска с номерами возможных ходов\n' 

def test__create_board__return_empty_board():
    assert create_board() == [' '] * 9

def test__draw_board__return_board_if_x_on_board():
    assert draw_board(['X',' ',' ',' ',' ',' ',' ',' ',' ']) == 'X| | \n=====\n | | \n=====\n | | ' 

def test__draw_board__return_board_if_o_on_board():
    assert draw_board(['O',' ',' ',' ',' ',' ',' ',' ',' ']) == 'O| | \n=====\n | | \n=====\n | | '     

def test__draw_board__return_board_if_x_and_o_on_board():
    assert draw_board([' ','X','O',' ','X',' ','O',' ',' ']) == ' |X|O\n=====\n |X| \n=====\nO| | '

def test__check_win_extracted__return_if_win_at_row():
    assert check_win_extracted(['X','X','X',' ',' ',' ',' ',' ',' '], 'X') == True

def test__check_win_extracted__return_if_win_at_column():
    assert check_win_extracted(['X',' ',' ','X',' ',' ','X',' ',' '], 'X') == True

def test__check_win_extracted__return_if_win_at_crossline():
    assert check_win_extracted(['X',' ',' ',' ','X',' ',' ',' ','X'], 'X') == True

def test__check_win_extracted__return_if_not_win():
    assert check_win_extracted(['X',' ',' ',' ',' ',' ','X',' ',' '], 'X') == False

def test__check_win__return_if_user_win():
    assert check_win(['X','X','X',' ',' ',' ',' ',' ',' '], 'X') == 'Победил пользователь!'

def test__check_win__return_if_pc_win():
    assert check_win(['X','X','X',' ',' ',' ',' ',' ',' '], 'O') == 'Победил компьютер!'

def test__check_win__return_if_user_and_pc_not_win():
    assert check_win(['X','X',' ',' ',' ',' ',' ',' ',' '], 'O') == None