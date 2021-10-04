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

def choice_input():
  """
  Ask user whether the user wants to play for "X" or "O"
  Checks whether the input is correct
  Ruterns the users input to the display
  """

  marker =''
  while not (marker == 'X' or marker == "O"):
    marker = input('Human! Do you want to play for "X" or "O"?\n').upper()
  if marker == "X":
    print('Human you decided to play for "X".')
    return ('X', "O")
  else:
    print('Human, you decided to play for "O".')
    return('O', 'X')

choice_input()