from tictactoe_objects import choose_first, player_input, player_choice, display_board, place_marker, win_check, replay, \
    full_board_check


print('Welcome to Tic Tac Toe!')

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board_new = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

full = False
game_on = True
counter = True

# display starting board
display_board(board)
# asks for marker
marker = player_input()
# prints beginners message
print(f"Player {choose_first()} starts!")
# starting player dependent on choose_first()
if int(choose_first()) == 1:
    counter = True
else:
    counter = False

while game_on:
    # Set the game up here

    # Player 1 Turn
    if counter:
        # Calls for players input
        player1 = int(player_choice(board))
        # place marker
        place_marker(board, marker[0], player1)
        # change counter
        counter = False
        # display board
        display_board(board)
        # win condition
        if win_check(board, marker[0]):
            print("Game Over! Player 1 Won!")
            # asks if they want to replay
            if not replay():
                game_on = False
            else:
                game_on = True
                # resets the game board
                board = board_new
                display_board(board)

    # Player 2 Turn
    elif not counter:
        # calls for player input
        player2 = int(player_choice(board))
        # place marker
        place_marker(board, marker[1], player2)
        # change counter
        counter = True
        # display gameboard
        display_board(board)
        # win condition
        if win_check(board, marker[1]):
            print("Game Over! Player 2 Won!")
            # asks if they want to replay
            if not replay():
                game_on = False
            else:
                game_on = True
                board = board_new
                display_board(board)

    # Check if board is full - results in  tie
    if full_board_check(board):
        print("Game Over! Tie!")

        # asks if they want to replay
        if not replay():
            game_on = False
        else:
            game_on = True
            board = board_new
            display_board(board)

    # if not replay():
    # break