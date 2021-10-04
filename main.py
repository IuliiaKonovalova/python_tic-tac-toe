from IPython.display import clear_output
from random import randint

def display_board(board):
    clear_output()

    """
    Prints an empty playing board to the user
    """
    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

board_positions = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

board_new = ['0', '*', '*', '*', '*', '*', '*', '*', '*', '*']



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



def win_check(board, mark):
  """
  Tests whether there is a win
  """
  return ((board[1] == mark and board[2] == mark and board[3] == mark) or
  (board[4] == mark and board[5] == mark and board[6] == mark) or
  (board[7] == mark and board[8] == mark and board[9] == mark) or
  (board[1] == mark and board[5] == mark and board[9] == mark) or
  (board[3] == mark and board[5] == mark and board[7] == mark) or
  (board[1] == mark and board[4] == mark and board[7] == mark) or
  (board[2] == mark and board[5] == mark and board[8] == mark) or
  (board[3] == mark and board[6] == mark and board[9] == mark))



def who_goes_first():
  """
  Allows user to choose who will go first: computer or the user
  Provides the option to randomly choose who plays first
  Provides the option to choose who goes first by the user
  """
  agreement = ''
  while not (agreement == 'Y' or agreement == 'N'):
    agreement = input('Do you agree to randomly decide who goes first?\n\nType"Y" if you agree\nType "N" if want to decide be yourself\n').upper()
  
  if agreement == 'Y':
    if randint(0, 1) == 0:
      print('Human goes first')
      return 'Human goes first'
    else:
      print('Computer goes first')
      return 'Computer goes first'
  else:
    human_choice = input('Your call...\n\nPrint "C" if you want me to go first.\nPrint "H" if you want to go first.\n').upper()
    while not (human_choice == 'C' or human_choice == 'H'):
      return human_choice
    if human_choice == 'H':
      print('Human goes first')
      return 'Human goes first'
    else:
      print('Computer goes first')
      return 'Computer goes first'


def start_game():
  """
  Asks the user whether the user is ready to start playing
  """
  play_game = input('Are you ready to play?\nEnter "Y" or "N".\n').upper()
  while not (play_game == "Y" or play_game == "N"):
    return play_game
  if play_game == 'Y':
    return True
  else:
    return False


def space_check(board, position):
  """
  Checks whether the board cell is available
  """
  return board[position] == ' '

def full_board_check(board):
  """
  Checks whether the board is full
  If full, returns true
  """
  for i in range(1,10):
    if space_check(board, i):
      return False
  return True



def main_game():
  print('Welcome to Tic Tac Toe with me!\n\nThis is the play board.\nPay attention to the positions of cells!')

  board_reset = [' '] * 10

  display_board(board_positions)
  choice = choice_input()
  turn = who_goes_first()
  display_board(board_reset)
  playing = start_game()



main_game()
