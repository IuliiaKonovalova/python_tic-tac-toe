from IPython.display import clear_output
from random import randint, shuffle

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
    return marker
  else:
    print('Human, you decided to play for "O".')
    return marker



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


def player_choice(board):

  """
  Asks the user for the next position
  Checks whether is input is correct
  Checks whether the place is available
  """
  position = 0
    
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    position = int(input('Choose your next position: (1-9) '))
        
  return position

def place_marker(board, marker, position):
    
    board[position] = marker

def computer_choice(board):
  """
  Answers by the computer
  """
  position = 0
  comp_core_guesses = [1, 3, 7, 9]
  shuffle(comp_core_guesses)
  comp_additional_guesses = [2, 4, 6, 7]
  shuffle(comp_additional_guesses)
  if space_check(board, 5):
    position = 5
    print(position)
    return position
  elif space_check(board, comp_core_guesses[0]):
    position = comp_core_guesses[0]
    print(position)
    return position
  elif space_check(board, comp_core_guesses[1]):
    position = comp_core_guesses[1]
    print(position)
    return position
  elif space_check(board, comp_core_guesses[2]):
    position = comp_core_guesses[2]
    print(position)
    return position
  elif space_check(board, comp_core_guesses[3]):
    position = comp_core_guesses[3]
    print(position)
    return position
  elif not space_check(board, 1) and not space_check(board, 3) and not space_check(board, 7) and not space_check(board, 9) and not space_check(board, 5):
    print("1, 3, 5, 7, 9 are not available")
    
    if space_check(board, comp_additional_guesses[0]):
      position = comp_additional_guesses[0]
      print(position)
      return position
    elif space_check(board, comp_additional_guesses[1]):
      position = comp_additional_guesses[1]
      print(position)
      return position
    elif space_check(board, comp_additional_guesses[2]):
      position = comp_additional_guesses[2]
      print(position)
      return position
    elif space_check(board, comp_additional_guesses[3]):
      position = comp_additional_guesses[3]
      print(position)
      return position




def main_game():
  print('Welcome to Tic Tac Toe with me!\n\nThis is the play board.\nPay attention to the positions of cells!')

  board_reset = [' '] * 10

  # Show the positions on the board
  display_board(board_positions)

  # Assigning markers for players
  choice = choice_input()
  human_marker = ''
  computer_marker = ''
  if choice == 'X':
    human_marker = 'X'
    computer_marker = 'O'
  else:
    human_marker = 'O'
    computer_marker = 'X'

  #Decide how goes is the first player 
  turn = who_goes_first()

  # Show empty board
  display_board(board_reset)

  # Asking the user to start the game
  playing = start_game()

  # If the user confirm "start the game" play the game
  while playing:

    # If computer's turn
    if turn == 'Computer goes first':
      print('My turn')
      position = computer_choice(board_reset)
      place_marker(board_reset, computer_marker, position)
      display_board(board_reset)

      if win_check(board_reset, choice):
        display_board(board_reset)
        print('Congratulations ME! I have won the game!')
        playing = False
      else:
        if full_board_check(board_reset):
          display_board(board_reset)
          print('The game is a draw!')
          break
        else:
          print('Your turn, Human!')
          turn = 'Human goes first'
    
    #  If player's turn
    else:
      print('Your turn...')
      position = player_choice(board_reset)
      place_marker(board_reset, human_marker, position)
      display_board(board_reset)
      if win_check(board_reset, choice):
        display_board(board_reset)
        print('Congratulations! You have won the game!')
        playing = False
      else:
        if full_board_check(board_reset):
          display_board(board_reset)
          print('The game is a draw!')
          break
        else:
          print('My turn, Human!')
          turn = 'Computer goes first'



main_game()
