from IPython.display import clear_output

def display_board(board):
    clear_output()

    """
    Prints an empty playing board to the user
    """
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


new_board = ['0', '*', '*', '*', '*', '*', '*', '*', '*', '*']

display_board(new_board)