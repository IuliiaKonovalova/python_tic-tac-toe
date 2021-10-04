from IPython.display import clear_output
from random import randint

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
    print('Human, you decided to play for "X".')
    return ('X', "O")
  else:
    print('Human, you decided to play for "O".')
    return('O', 'X')

choice_input()

def win_check(board, mark):
  """
  Tests whether there is a win
  """
  return ((board[7] == mark and board[8] == mark and board[9] == mark) or
  (board[4] == mark and board[5] == mark and board[6] == mark) or
  (board[1] == mark and board[2] == mark and board[3] == mark) or
  (board[7] == mark and board[5] == mark and board[3] == mark) or
  (board[9] == mark and board[5] == mark and board[1] == mark) or
  (board[7] == mark and board[4] == mark and board[1] == mark) or
  (board[8] == mark and board[5] == mark and board[2] == mark) or
  (board[9] == mark and board[6] == mark and board[3] == mark))

win_check(new_board, 'X')

def who_goes_first():
  """
  Allows user to choose who will go first: computer or the user
  Provides the option to randomly choose who plays first
  Provides the option to choose who goes first by the user
  """
  agreement = ''
  while not (agreement == 'Y' or agreement == 'N'):
    agreement = input('Do you agree to randomly decide who goes first?\nType"Y" if you agree\nType "N" if want to decide be yourself\n').upper()
  
  if agreement == 'Y':
    if randint(0, 1) == 0:
      print('Human goes first')
      return 'Human goes first'
    else:
      print('Computer goes first')
      return 'Computer goes first'
  else:
    human_choice = input('You call...\nPrint "C" if you want me to go first.\n "Print "H" if you want to go first.\n').upper()
    while not (human_choice == 'C' or human_choice == 'H'):
      return human_choice
    if human_choice == 'H':
      print('Human goes first')
      return 'Human goes first'
    else:
      print('Computer goes first')
      return 'Computer goes first'

who_goes_first()