from IPython.display import clear_output
from random import randint
def welcome_message():

    # Welcome player to the game
    # and print some game info
    print('Welcome to the Tic Tac Toe game!')
    print('First, choose your own marker.')
    print('Second, choose your position (number 1-9 corresponds with a number on a number pad) to place your marker.')
    print('Finally, whoever gets three his/her markers in a row wins the game.')
    print('Or if all 9 squares are full but no one has three in a row, the game is over!')
    print("Let's play!!")

def display_board(board):
    clear_output()  # This only works in jupyter!

    # print out the board
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_marker():

    marker1 = ''

    # let player1 choose the marker
    while marker1.upper() != 'X' and marker1.upper() != 'O':
        marker1 = input('Player1, please choose your marker(X or O): ')

    # assign player2 the other marker
    if marker1.upper() == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'

    # return marker1 and marker2 representing player1 and player2 respectively.
    return (marker1.upper(), marker2.upper())

def who_goes_first():

    # Assume 0 represents player1 and 1 represent player2
    if randint(0,1) == 0:
        print('Player1 will go first!')
        return 'Player1'
    else:
        print('Player2 will go first!')
        return 'Player2'

def place_marker(board, marker):

    position = ''

    # Prompt the player to place his/her marker
    # check if the input is valid
    while position not in range(1,10) or board[position] == 'X' or board[position] == 'O':

        # take in player input
        position = int(input('Please enter 1-9 to place your marker: '))

        # tell the player why the input is invalid
        if position not in range(1,10):
            print('Sorry, invalid input!')
        else:
            pass
        if board[position] == 'X' or board[position] == 'O':
            print('Sorry, the position was marked already!')
        else:
            pass

    # place the marker
    board[position] = marker

    # Keep the board updated
    return board

def is_game_over(board, round_count, marker, player1):

    # Check if the game is over
    if ((board[1] == board[2] == board[3]) or # across the bottom
        (board[4] == board[5] == board[6]) or # across the middle
        (board[7] == board[8] == board[9]) or # across the top
        (board[1] == board[5] == board[9]) or # diagonal
        (board[3] == board[5] == board[7]) or # diagonal
        (board[1] == board[4] == board[7]) or # down the left side
        (board[2] == board[5] == board[8]) or # down the middle
        (board[3] == board[6] == board[9])):  # down the right side

        # check who wins the game
        if marker == player1:
            print('Congrats! Player1 is the winner!')
        else:
            print('Congrats! Player2 is the winner!')
        return True
    # if all 9 squares are full, print game over message
    elif round_count == 9:
        print('The game is over, you guys are tie!')
        return True
    # else the game is not over yet
    else:
        return False

def play_again():

    again = ''

    # Check if the input is valid
    while again.upper() != 'Y' and again.upper() != 'N':
        again = input("Play again('Y' or 'N'): ")
        if again.upper() != 'Y' and again.upper() != 'N':
            print('Sorry, invalid input!')
        else:
            pass

    # return true if the players want to play again,
    # otherwise, return false
    if again.upper() == 'Y':
        return True
    else:
        return False

def game_driver():

    # Welcome the players
    welcome_message()

    # Hold if keep playing or not
    keep_playing = True

    # Check if playing again
    while keep_playing:

        # Hold if the game is over
        game_over = False

        # Reset the board
        board = ['S', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # set the specific marker to palyer1 and player2
        (player1, player2) = player_marker()

        # Randomly choose who goes first
        if who_goes_first() == 'Player1':

            # list for deciding who goes next
            switch_turn = [player1.upper()]
        else:
            switch_turn = [player2.upper()]

        # count the turns of the game
        count_turn = 0

        # Check if game is over
        while game_over == False:

            # Update the board
            board = place_marker(board, switch_turn[-1])

            # Display board everytime players place their marker
            display_board(board)

            # Update the count of the turn
            count_turn += 1

            # Check who places the last marker and decide who goes next
            if switch_turn[-1] == player1:
                print('Player2 is your turn!')
                switch_turn += player2.upper()
            else:
                print('Player1 is your turn!')
                switch_turn += player1.upper()

            # Update if game is over everytime players place their markers
            game_over = is_game_over(board, count_turn, switch_turn[-2], player1)

        # Update if keep playing
        keep_playing = play_again()

    # Farewell message
    if keep_playing == False:
        print('Thank you for playing our game!')
        print('Hope you enjoy it!')
        print('See you next time:)')
