def board_drawing() -> None:
    print('1|2|3')
    print('=====')
    print('4|5|6')
    print('=====')
    print('7|8|9')

def start_condition() -> str:
    first_line = ' | | \n'
    second_line = '=====\n'
    third_line = ' | | \n'
    furth_line = '=====\n'
    fifth_line = ' | | '
    all_lines = first_line + second_line + third_line + furth_line + fifth_line
    return all_lines

def draw_board(my_list: list[str]) -> str:
    line_one = '|'.join(my_list[0:3])
    line_two = '|'.join(my_list[3:6])
    line_three = '|'.join(my_list[6:9])
    new_line = []
    new_line.append(line_one)
    new_line.append(line_two)
    new_line.append(line_three)
    
    return '\n=====\n'.join(new_line)

if __name__ == '__main__':
    board_drawing()
    my_list = ['X',' ',' ',' ',' ',' ',' ',' ',' ']
    draw_board(my_list)
