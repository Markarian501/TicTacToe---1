import random


def display_board(board):
    print(board[1:4])
    print(board[4:7])
    print(board[7:10])
    pass


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    pass


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    code = [f'{mark}', f'{mark}', f'{mark}']
    diagonal1 = [board[1], board[5], board[9]]
    diagonal2 = [board[3], board[5], board[7]]

    result = False
    loopcounter = 1

    for num in [1, 2, 3]:
        if board[loopcounter:loopcounter + 3] == code:
            result = True
        else:
            loopcounter += 3
    for num in [1, 2, 3]:
        vertical = [board[num], board[num + 3], board[num + 6]]
        if vertical == code:
            result = True
    if diagonal1 == code:
        result = True
    elif diagonal2 == code:
        result = True

    return result

    pass


def choose_first():
    return random.randint(1, 2)
    pass


def space_check(board, position):
    result = False
    if board[position] == ' ':
        result = True
    else:
        result = False

    return result

    pass


def full_board_check(board):
    result = False
    full_board = []
    for index in board:
        if index != ' ':
            full_board.append(True)
        else:
            full_board.append(False)
    if all(full_board):
        result = True
    else:
        result = False

    return result

    pass


def player_choice(board):
    choice = 'WRONG'
    within_range = False
    position = False

    while choice.isdigit() == False or within_range == False or position == False:

        choice = input("Select the next position: ")
        if not choice.isdigit():
            print("Please enter a number!")

        if choice.isdigit():
            if int(choice) in range(0, 10):
                within_range = True
                if space_check(board, int(choice)):
                    position = True
                else:
                    print("Position occupied! Select another position")
                    position = False
            else:
                within_range = False

    return choice
    pass


def replay():
    player_answer = "Wrong"
    retry = False

    while retry == False and player_answer.isdigit() == False:
        player_answer = input("Would you like to play again? Select 1 for Yes or 2 for No: ")
        if not player_answer.isdigit():
            print("Please select 1 or 2")
        elif player_answer.isdigit():
            if int(player_answer) in range(1, 3):
                if int(player_answer) == 1:
                    retry = True
                if int(player_answer) == 2:
                    retry = False

            else:
                print("Please select 1 or 2")
                player_answer = "Wrong"
    return retry
    pass
