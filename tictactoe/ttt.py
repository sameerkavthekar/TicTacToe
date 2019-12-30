import random

def display_board(board):
    
    print('\n'*100)
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |   ')

def player_input():
    
    n1=''
    while not(n1=='X' or n1=='O'):
        n1 = input("Player 1 choose X or O marker: ").upper()
    if n1 == 'X':
        return ['X','O']
    else:
        return ['O','X']

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[7]==mark and board[4]==mark and board[1]==mark) or
            (board[8]==mark and board[5]==mark and board[2]==mark) or
            (board[9]==mark and board[6]==mark and board[3]==mark) or
            (board[7]==mark and board[5]==mark and board[3]==mark) or
            (board[1]==mark and board[5]==mark and board[9]==mark))

def choose_first():

    n = random.randint(0,1)
    if n == 1:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    
    if board[position]==' ':
        return True
    else:
        return False

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9): '))
        
    return position

def replay():

    o=''
    while not(o=='Y' or o == 'N'):
        o = input("Do you want to play again: Enter Y or N: ")
    if o=='Y':
        return True

print('Welcome to Tic Tac Toe!')

while True:
    
    board = [' ']*10
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print(turn+' will go first')

    play_game = input("\nAre you ready to play the game: Enter Y or N : ")

    if play_game.upper()=='Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_mark,position)
            if win_check(board,player1_mark):
                display_board(board)
                print("\nCongrats Player 1 you have won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('\nGame is a draw')
                    break
                else:
                    turn = 'Player 2'
        else:

            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_mark, position)

            if win_check(board, player2_mark):
                display_board(board)
                print('\nPlayer 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('\nThe game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break