from IPython.display import clear_output
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
