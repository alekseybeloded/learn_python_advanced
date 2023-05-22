from random import choice


def start_draw_board() -> str:
    first_line = '1|2|3\n'
    second_line = '=====\n'
    third_line = '4|5|6\n'
    fourth_line = '=====\n'
    fifth_line = '7|8|9\n'
    sixth_line = 'Выше изображена игральная доска с номерами возможных ходов\n'
    all_lines = first_line + second_line + third_line + fourth_line + fifth_line + sixth_line
    return all_lines

def user_input() -> str:
    user_input = input('Сделайте свой ход - введите значение от 1 до 9\n')
    return int(user_input)

def pc_input(moves: list[int]) -> int:
    cells = {i for i in range(1, 10)}
    free_cells = cells - set(moves)
    return choice(list(free_cells))

def choose_user_symbol() -> str:
    return choice(['X','O'])

def create_board() -> list[str]:
    return [' '] * 9

def set_symbol(board: list[str], cell: int, symbol: str) -> None:
    board[cell - 1] = symbol

def draw_board(current_condition_board: list[str]) -> str:
    board_part_one = '|'.join(current_condition_board[0:3])
    board_part_two = '|'.join(current_condition_board[3:6])
    board_part_three = '|'.join(current_condition_board[6:9])
    result_board = []
    result_board.append(board_part_one)
    result_board.append(board_part_two)
    result_board.append(board_part_three)
    return '\n=====\n'.join(result_board)

def check_win_extracted(board: list[str], user_symbol: str) -> bool:
    rows = [
        board[:3],
        board[3:6],
        board[7:],
    ]
    
    if any([row == [user_symbol, user_symbol, user_symbol] for row in rows]):
        return True
    
    cols = [
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
    ]

    if any([col == [user_symbol, user_symbol, user_symbol] for col in cols]):
        return True
    
    crosslines = [
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    
    if any([crossline == [user_symbol, user_symbol, user_symbol] for crossline in crosslines]):
        return True

    return False
    
def check_win(board: list[str], user_symbol: str) -> str | None:
    if check_win_extracted(board, user_symbol=user_symbol):
        return 'Победил пользователь!'
    
    if check_win_extracted(board, user_symbol='O' if user_symbol == 'X' else 'X'):
        return 'Победил компьютер!'
        
    return None

def main() -> None:
    print(start_draw_board())
    user_symbol = choose_user_symbol()
    board = create_board()

    moves = []
    is_running = True

    while is_running:
        user_move = user_input()
        moves.append(user_move)
        set_symbol(board, user_move, user_symbol)
        print(draw_board(board))

        user_win_message = check_win(board, user_symbol)
        if user_win_message == 'Победил пользователь!' or user_win_message == 'Победил компьютер!':
            print(user_win_message)
            break

        print('Ход компьютера:')

        pc_move = pc_input(moves)
        moves.append(pc_move)
        set_symbol(board, pc_move, 'O' if user_symbol == 'X' else 'X')
        print(draw_board(board))

        user_win_message = check_win(board, user_symbol)
        if user_win_message == 'Победил пользователь!' or user_win_message == 'Победил компьютер!':
            print(user_win_message)
            break



if __name__ == '__main__':
    main()