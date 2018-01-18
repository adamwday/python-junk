#Allows us to clear the output for Jupyter Notebook
import random
from IPython.display import clear_output

#Function creates the board
def display_board(board):

    clear_output()
    print('   |   |  ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |  ')
    print('------------')
    print('   |   |  ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |  ')
    print('------------')
    print('   |   |  ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |  ')

#Function accepts player input and assign an "X" or an "O".
def player_input():

    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Function takes the desired position and adds it to the form.
def place_marker(board, marker, position):
    board[position] = marker

#Function takes in a board and a mark and checks to see if that mark as won the game.
def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  #across top
            (board[4] == mark and board[5] == mark and board[6] == mark)  or  #across middle
            (board[1] == mark and board[2] == mark and board[3] == mark)  or  #across bottom
            (board[7] == mark and board[5] == mark and board[3] == mark)  or  #diagonal left 2 right
            (board[9] == mark and board[5] == mark and board[1] == mark)  or  #diagonal right 2 left
            (board[7] == mark and board[4] == mark and board[1] == mark)  or  #down left
            (board[8] == mark and board[5] == mark and board[2] == mark)  or  #down middle
            (board[9] == mark and board[6] == mark and board[3] == mark))     #down right

#Uses a random module to decide which player goes first.
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#Function returns a boolean that indicates if a space on the board is available.
def space_check(board, position):

    return board[position] == ' '

#Function that checks if the board is full and returns a boolean value.
def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
        return True

#Function asks for the next player's position and uses the input from space_check function to see if it is a free position.
def player_choice(board):

    position = ' '

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):

        position = input('Choose your next position: (1-9) ')
    return int(position)

#Function that asks the player if they want to play again and returns a boolean.
def replay():

    return input('Do you want to play again? Enter Yes or No').lower().startswith('y')


#Function that runs the game.
print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    game_on = True

    while game_on:

        if turn == 'Player 1':

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations, Player 1, has won the game!')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations, Player 2, has won the game!')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
