from main import start_condition, draw_board

def test_start_condition_return_correct_board():
    assert start_condition() == ' | | \n=====\n | | \n=====\n | | ' 

def test_draw_board_return_correct_board_state1():
    assert draw_board(['X',' ',' ',' ',' ',' ',' ',' ',' ']) == 'X| | \n=====\n | | \n=====\n | | ' 

def test_draw_board_return_new_corrrect_board_state2():
    assert draw_board([' ','X',' ',' ',' ',' ',' ',' ',' ']) == ' |X| \n=====\n | | \n=====\n | | '     

def test_draw_board_return_new_corrrect_state3():
    assert draw_board([' ','X','O',' ','X',' ','O',' ',' ']) == ' |X|O\n=====\n |X| \n=====\nO| | '
