import os
import time
import random

def clear():
 os.system('clear')
def sleep(slp):
 return time.sleep(slp)
def rng(ra,rb):
 return random.uniform(ra,rb)
def contains(ca,cb):
 return list.__contains__(ca,cb)
def print_move():
 lines = 0
 print()
 if contains(can_up,position):
  print('  Up = "8"')
  lines = lines + 1
 if contains(can_left,position):
  print('  Left = "4"')
  lines = lines + 1
 if contains(can_down,position):
  print('  Down = "2"')
  lines = lines + 1
 if contains(can_right,position):
  print('  Right = "6"')
  lines = lines + 1
 for i in range((lines - lines * 2) + 4):
  print()
 print()
 print('  Quit and show generated data = "exit"')
def move():
 global position
 try:
  if goto == 8 and contains(can_up,position):
   position = position - 100
  elif goto == 4 and contains(can_left,position):
   position = position - 1
  elif goto == 2 and contains(can_down,position):
   position = position + 100
  elif goto == 6 and contains(can_right,position):
   position = position + 1
  show_error = False
 except:
  print('Input does have to be one of these numbers: "2","4","6","8".')
  show_error = True
 return position

show_error = False
position = 0
debug_pos = ''
debug_show_pos = True
key = 0
lock = 0
xxx = 0
msg1 = ''
msg1_pos = 0

def game():
 global position, goto, key, lock_pos, prefix, xxx, debug_show_pos, debug_pos, msg1, msg1_pos
 global lock_up, lock_down, lock_left, lock_right, can_up, can_left, can_down, can_right
 game_input = 42
 while(True):
  xxx = xxx +1
  prefix = ''
  if debug_show_pos:
   debug_pos = f'pos={position}, exit={exit}, lock_pos={lock_pos}, key_pos={key}'
  else:
   debug_pos = ''
  maze_icon()
  print_move()
  game_input = input('\n>>> ')
  if game_input == '888':
   can_up.append(position)
   can_down.append(position-100)
  if game_input == '444':
   can_left.append(position)
   can_right.append(position-1)
  if game_input == '222':
   can_down.append(position)
   can_up.append(position+100)
  if game_input == '666':
   can_right.append(position)
   can_left.append(position+1)
  if game_input == 'exit':
   clear()
   print('I recommend you to copy this to different file than the whole game so you can do it without errors.\n')
   z = 1
   for i in range(15):
    for i in range(15):
     if contains(can_left,z):
      if z < 10:
       print(f' 000{z}',end='')
      else:
       print(f' 00{z}',end='')
     else:
      if z < 10:
       print(f'|000{z}',end='')
      else:
       print(f'|00{z}',end='')
     z = z + 1
    print()
    z = z - 15
    for i in range(15):
     if contains(can_down,z):
      print('-    ',end='')
     else:
      print('-----',end='')
     z = z + 1
    print()
    z = 101

   print('\n')
   print(f'can_up = {can_up}')
   print(f'can_left = {can_left}')
   print(f'can_down = {can_down}')
   print(f'can_right = {can_right}')
   print()
   print(f'position = {position}')
   print()
   input('Press Enter to continue editing or Ctrl+C to exit when copied')
  if game_input == 'debug' or game_input == '555':
   debug_exit = False
   clear()
   print('  *** Debug Section ***')
   if debug_exit == False:
    while(True):
     print('  1 = set "debug_show_pos" to True\n  2 = set "debug_show_pos" to False\n  3 = teleport to\n  exit = to exit (wow)')
     debug_input = input('>>> ')
     if debug_input == 'exit':
      break
     elif debug_input == '1':
      debug_show_pos = True
     elif debug_input == '2':
      debug_show_pos = False
     elif debug_input == '3':
      print('Teleport to position:')
      iinnppuutt = input('> ')
      try:
       position = int(iinnppuutt)
       break
      except:
       print('This was not a number')
 
  try:
   goto = int(game_input)
  except:
   print('Input does have to be one of these inputs: "2","4","6","8", or "exit".')
   prefix = 'Input does have to be one of these inputs: "2","4","6","8", or "exit".'
  position = move()

def maze_icon():
 global prefix, xxx, debug_pos
 space='       '
# up
 if contains(can_left,position-100) == False:
  line_Ub = '  |'
 else:
  line_Ub = '   '
 if contains(can_right,position-100) == False:
  line_Uc = '|'
 else:
  line_Uc = ''
# down
 if contains(can_left,position+100) == False:
  line_Db = '  |'
 else:
  line_Db = '   '
 if contains(can_right,position+100) == False:
  line_Dc = '|'
 else:
  line_Dc = ''
# left
 if contains(can_up,position-1) == False:
  line_La = '--'
 else:
  line_La = '  '
 if contains(can_down,position-1) == False:
  line_Ld = '--'
 else:
  line_Ld = '  '
# right
 if contains(can_up,position+1) == False:
  line_Ra = '--'
 else:
  line_Ra = ''
 if contains(can_down,position+1) == False:
  line_Rd = '--'
 else:
  line_Rd = ''
# center
 if contains(can_up,position) == False:
  if position == lock_pos and lock_up:
   line_Ca = '-L-O-C-K-'
  else:
   line_Ca = '---------'
 else:
  line_Ca = '-       -'
 if contains(can_left,position) == False:
  if position == lock_pos and lock_left:
   line_CbA = 'LO'
   line_CbB = 'CK'
   line_CbC = ':)'
  else:
   line_CbA = ' |'
   line_CbB = ' |'
   line_CbC = ' |'
 else:
  line_CbA = '  '
  line_CbB = '  '
  line_CbC = '  '
 if contains(can_right,position) == False:
  if position == lock_pos and lock_right:
   line_CcA = 'LO'
   line_CcB = 'CK'
   line_CcC = ':)'
  else:
   line_CcA = '|'
   line_CcB = '|'
   line_CcC = '|'
 else:
  line_CcA = '  '
  line_CcB = '  '
  line_CcC = '  '
 if contains(can_down,position) == False:
  if position == lock_pos and lock_down:
   line_Cd = '-L-O-C-K-'
  else:
   line_Cd = '---------'
 else:
  line_Cd = '-       -'

 global l
 clear()
 for i in range(20):
  print()
 print(f' {prefix}\n{debug_pos}\n {line_Ub}{space}{line_Uc}\n {line_La}{line_Ca}{line_Ra}\n  {line_CbA}{space}{line_CcA}\n  {line_CbB}  You  {line_CcB}\n  {line_CbC}{space}{line_CcC}\n {line_Ld}{line_Cd}{line_Rd}\n {line_Db}{space}{line_Dc}')

def lock():
 global lock_up, lock_down, lock_left, lock_right
 if lock_up:
  can_up.append(lock_pos)
 if lock_down:
  can_down.append(lock_pos)
 if lock_left:
  can_left.append(lock_pos)
 if lock_right:
  can_right.append(lock_pos)

## The BurgerMaze
# Welcome and End screen
clear()
print('Welcome to the official BurgerMaze "Map Creator" by MrBurgerCZ.\nWith this tool, creating of new levels will be easier.\nIt is recommended to draw the map and then start using this tool.')
print()
print('You can move normally with "2", "4", "6", "8".\nTo make a new hole in the wall, the controls are simple:\n Press the movement key ("2", "4", ...) 3 times (like "222", "444", ...) instead of single press and then hit Enter.\nPlease do *not* go into *negative* values.')
print('You can enter the debug section by typing "debug" or "555".')
print()
print('I hope you will enjoy this tool.\n\nPlease, enter the spawn location (last two numbers are columns, first numbers are lines. Example: line 1 and column 7 is 107, line 32 and column 71 is 3271):')
position=int(input('>>> '))
while(True):

 can_up = []
 can_down = []
 can_left = []
 can_right = []

 exit = 0
 lock_pos = 0
 lock_up = False
 lock_down = False
 lock_left = False
 lock_right = False

 clear()
 game()
