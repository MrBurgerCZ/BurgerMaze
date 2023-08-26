### BurgerMaze - game by MrBurgerCZ (c) 2023 ###

#          _____________________________________
#         /#####################################
#        /#                                  /#
#       /#  mail       mrburgercz@gmail.com /#
#      /#  GitHub     MrBurgerCZ           /#
#     /#  reddit     u/MrBurgerCZ         /#
#    /#  Discord    @mrburgercz          /#
#   /#  Instagram  @mrburgercz          /#
#  /#__________________________________/#
# /#####################################


## First, we will import needed libraries
try:
 import os
 print('[Info] Module "os" was imported successfully')
except:
 print('[Error] Module "os" cannot be imported')
try:
 import time
 print('[Info] Module "time" was imported successfully')
except:
 print('[Error] Module "time" cannot be imported')
try:
 import random
 print('[Info] Module "random" was imported successfully')
except:
 print('[Error] Module "random" cannot be imported')

## Then, we will make some actions easier to do
def clear():
 try:
  os.system('clear')
 except:
  print('\n\n\n\n\n\n\n\n')
  print('\n\n\n\n\n\n\n\n')
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
 print('  Quit = "exit"')
 if show_error:
  print('Input does have to be one of these inputs: "2","4","6","8", or "exit".')
  prefix = 'Input does have to be one of these inputs: "2","4","6","8", or "exit".'
def move():
 global position
 try:
  if goto == 8 and contains(can_up,position):
   position = position - 10
  elif goto == 4 and contains(can_left,position):
   position = position - 1
  elif goto == 2 and contains(can_down,position):
   position = position + 10
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
debug_show_pos = False
key = 0
lock = 0
xxx = 0
try:
 s = os.get_terminal_size()
 l = s.lines
 coll = s.columns
 print(f'[Info] Terminal size [{l}x{coll}] detected')
except:
 l = 0
 coll = 0
 print("[Error] os.get_terminal_size() didn't work as expected")
def game():
 global position, goto, key, lock_pos, inv_key, prefix, xxx, debug_show_pos, debug_pos, msg1, msg1_pos
 global lock_up, lock_down, lock_left, lock_right
 game_input = 42
 while(True):
  xxx = xxx +1
  prefix = ''
  if position == exit:
   maze_icon()
   print('\n#########################\n# You found the Exit!!! #\n#########################\n')
   break
  if position == key:
   inv_key = True
   prefix = 'You found the key!'
  if position == msg1_pos:
   prefix = msg1
  if position == lock_pos:
   if inv_key:
    lock()
   else:
    prefix = 'You must have a key to unlock this lock!'
  if debug_show_pos:
   debug_pos = f'pos={position}, exit={exit}, lock_pos={lock_pos}, key_pos={key}'
  else:
   debug_pos = ''
  maze_icon()
  print_move()
  game_input = input('\n>>> ')
  if game_input == 'exit':
   break
  if game_input == 'debug':
   debug_exit = False
   clear()
   print('  *** Debug Section ***')
   print(' Enter the debug password')
   while(True):
    password = input('>>> ')
    if password == 'burgeristhebest' or password == '‱':
     break
    elif password == 'exit':
     debug_exit = True
     break
    else:
     print(' Wrong password! Try again')
   if debug_exit == False:
    print(' Logged in successfully')
    while(True):
     print('  1 = set "debug_show_pos" to True\n  2 = set "debug_show_pos" to False\n 3 = teleport to\n  exit = to start the GOD MODE')
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
 if contains(can_left,position-10) == False:
  line_Ub = '  |'
 else:
  line_Ub = '   '
 if contains(can_right,position-10) == False:
  line_Uc = '|'
 else:
  line_Uc = ''
# down
 if contains(can_left,position+10) == False:
  line_Db = '  |'
 else:
  line_Db = '   '
 if contains(can_right,position+10) == False:
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
 if xxx == 6:
  clear()
  xxx = 0
 else:
  print('\n\n\n\n\n\n\n\n\n\n\n\n')
 for i in range(l - 18):
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
sleep(0.8)
clear()
try:
 print('\n\n\n')
 for i in range(int((coll - 44)/2)):
  print(' ',end='')
 print('############################################')
 for i in range(int((coll - 44)/2)):
  print(' ',end='')
 print('# BurgerMaze - game by MrBurgerCZ (c) 2023 #')
 for i in range(int((coll - 44)/2)):
  print(' ',end='')
 print('############################################')
 print('\n\n          _____________________________________\n         /#####################################\n        /#                                  /#\n       /#  mail       mrburgercz@gmail.com /#\n      /#  GitHub     MrBurgerCZ           /#\n     /#  reddit     u/MrBurgerCZ         /#\n    /#  Discord    @mrburgercz          /#\n   /#  Instagram  @mrburgercz          /#\n  /#__________________________________/#\n /#####################################\n')
except:
 print()
 print('  ############################################')
 print('  # BurgerMaze - game by MrBurgerCZ (c) 2023 #')
 print('  ############################################')
 print()
quit = False
while(True):
 xxx = 0
 if quit:
  try:
   print('\n\n\n\n\n\n\n\n')
   for i in range(int((coll - 44)/2)):
    print(' ',end='')
   print('############################################')
   for i in range(int((coll - 44)/2)):
    print(' ',end='')
   print('# BurgerMaze - game by MrBurgerCZ (c) 2023 #')
   for i in range(int((coll - 44)/2)):
    print(' ',end='')
   print('############################################')
   for i in range(int((coll - 44)/2)):
    print(' ',end='')
  except:
   print()
   print('  ############################################')
   print('  # BurgerMaze - game by MrBurgerCZ (c) 2023 #')
   print('  ############################################')
   print()
  print('       Thank you for playing my game!\n\n\n\n\n\n\n\n')
  break

# Level picker
 run_maze = 0
 while(True):
  global lock_pos
  print('\nChoose a level:\n Level 1 - simple\n Level 2 - easy\n Level 3 - easy\n Level 4 - normal\n Level 5\n Level 6\n Level 7\n Level 8\n\nType "exit" to quit.')
  run_maze = input('> ')
  try:
   run_maze_nr = int(run_maze)
  except:
   run_maze_nr = 0
  if run_maze_nr == 70923081800910:
   run_maze_nr = 0
   run_maze = 'debug'
  if run_maze_nr != 0:
   break
  if run_maze == 'exit':
   quit = True
   break
  if run_maze == 'MrBurgerCZ':
   print('Hello there')
   sleep(2)
  if run_maze == 'hello there' or run_maze == 'Hello there':
   sleep(1)
   print('General Kenobi')
   sleep(2)
  if run_maze == 'debug':
   debug_exit = False
   clear()
   print('  *** Debug Section ***')
   print(' Enter the debug password')
   while(True):
    password = input('>>> ')
    if password == 'burgeristhebest' or password == '‱':
     break
    elif password == 'exit':
     debug_exit = True
     break
    else:
     print(' Wrong password! Try again')
   if debug_exit == False:
    print('# 01   02 | 03 | 04   05\n#    ------    ------\n# 11 | 12   13   14 | 15\n# ----    -    -    ----\n# 21   22   23   24   25\n# ----    -    -    ----\n# 31 | 32   33   34 | 35\n#    ------    ------\n# 41   42 | 43 | 44   45')
    run_maze_nr = 70923081800910
    break
  lock_pos = 0

# Maze 1

## Here is room layout
# 01   02   03 | 04
#    ------    -
# 11   12 | 13   14
#    ------    -
# 21 | 22 | 23 | 24
#    -    -    ----
# 31 | 32   33   34

 if run_maze_nr == 1:

  can_up = [11,13,14,21,23,24,31,32,33]
  can_down = [1,3,4,11,13,14,21,22,23]
  can_left = [2,3,12,14,33,34]
  can_right = [1,2,11,13,32,33]

  position = 2
  exit = 22
  lock_pos = 0
  lock_up = False
  lock_down = False
  lock_left = False
  lock_right = False

  clear()
  game()

 elif run_maze_nr == 128:
  clear()
  print('Franky Wild\nFranta Divoký\nJaký žw je to číŝlo? (pojď!)\nStodvacet, osum osum osum osum osum...')
  input()

# Maze 2

## Here is room layout
# 01 | 02 | 03   04   05   06
#    -    ------    -    -----
# 11   12   13   14 | 15 | 16
#    ----------------    -
# 21 | 22   23   24   25   26
# ----    ----------------
# 31 | 32   33 | 34 | 35 | 36
#    ------    -    -    -
# 41   42   43 | 44   45   46

 elif run_maze_nr == 2:

  can_up = [11,12,14,15,21,25,26,32,36,41,43,44,45,46]
  can_down = [1,2,4,5,11,15,16,22,26,31,33,34,35,36]
  can_left = [4,5,6,12,13,14,23,24,25,26,33,42,43,45,46]
  can_right = [3,4,5,11,12,13,22,23,24,25,32,41,42,44,45]

  position = 35
  exit = 2
  lock_pos = 0
  lock_up = False
  lock_down = False
  lock_left = False
  lock_right = False

  clear()
  game()

 elif run_maze_nr == 42:
  clear()
  print('Odpověď na otázku života, vesmíru a vůbec.')
  input()

# Maze 3

## Here is room layout
# 01 | 02   03   04   05 | 06   07   08   09
#    -    ------    ------    ------    -
# 11 | 12 | 13 | 14   15   16 | 17 | 18 | 19
# ---------    -    ------    -    -    -
# 21   22 | 23   24   25 | 26   27 | 28 | 29
#    -    ----------------    ------    ----
# 31 | 32   33   34 | 35   36 | 37   38 | 39
#    ------    -    -----------    ---------
# 41   42 | 43 | 44 | 45   46   47 | 48 | 49
#    ------    -    -    -    ------    -
# 51 | 52   53 | 54   55   56   57 | 58 | 59
#    ------    -----------    ------    -
# 61 | 62   63 | 64 | 65   66   67   68 | 69
#    -----------    -----------    ------
# 71   72   73 | 74   75   76 | 77 | 78   79
# ---------    -    ------    ------    ----
# 81   82   83   84   85 | 86   87   88 | 89

 elif run_maze_nr == 3:

  can_up = [11,12,14,16,18,19,23,24,26,27,28,29,31,32,36,38,41,43,44,47,51,53,54,55,56,58,59,61,63,66,68,69,71,74,77,79,83,84,86,88]
  can_down = [1,2,4,6,8,9,13,14,16,17,18,19,21,22,26,28,31,33,34,37,41,43,44,45,46,48,49,51,53,56,58,59,61,64,67,69,73,74,76,78]
  can_left = [3,4,5,7,8,9,15,16,22,24,25,27,33,34,36,38,42,46,47,53,55,56,57,63,66,67,68,72,73,75,76,79,82,83,84,85,87,88]
  can_right = [2,3,4,6,7,8,14,15,21,23,24,26,32,33,35,37,41,45,46,52,54,55,56,62,65,66,67,71,72,74,75,78,81,82,83,84,86,87]

  position = 17
  exit = 49
  lock_pos = 0
  lock_up = False
  lock_down = False
  lock_left = False
  lock_right = False

  clear()
  game()

# Maze 4

# 01 | 02   S3   04 | 05   06   07   08   09
#    -    -    ------    ----------------
# 11 | 12 | 13 | 14   15 | 16   17   18 | 19
#    -    -    ------    -    ------    -
# 21   22 | 23   24   25   26 | 27 | 28   29
# ----    ---------------------    -    -
# 31   32   33 | 34 | 35   36 | 37   38 | 39
#    ------    -    -    -    -    ------
# 41 | L2   43 | 44   45 | 46 | 47 | 48   49
#    -    ------    ------    -    ------
# 51 | 52   53   54 | 55   56 | 57 | K8   59
#    -    ------    ------    -----------
# 61 | 62   63 | 64 | 65 | 66 | 67 | 68   69
#    ----------------    -    -    ------
# 71   72 | 73 | 74   75 | E6 | 77   78 | 79
#    ------    -    -----------    -    -
# 81   82   83   84   85   86   87 | 88   89

 elif run_maze_nr == 4:
  can_up = [11,12,13,15,19,21,22,23,25,26,28,29,32,37,38,39,41,43,44,45,46,47,49,51,52,54,56,57,59,61,62,64,66,69,71,75,76,77,79,81,83,84,87,88,89]
  can_down = [1,2,3,5,9,11,12,13,15,16,18,19,22,27,28,29,31,33,34,35,36,37,39,41,44,46,47,49,51,52,54,56,59,61,65,66,67,69,71,73,74,77,78,79]
  can_left = [3,4,6,7,8,9,15,17,18,22,24,25,26,29,32,33,36,38,43,45,49,53,54,56,59,63,69,72,75,78,82,83,84,85,86,87,89]
  can_right = [2,3,5,6,7,8,14,16,17,21,23,24,25,28,31,32,35,37,42,44,48,52,53,55,58,62,68,71,74,77,81,82,83,84,85,86,88]

  position = 3
  exit = 76
  key = 58
  lock_pos = 42
  inv_key = False
  lock_up = False
  lock_down = True
  lock_left = False
  lock_right = False

  clear()
  game()

# Maze 5

# 01   02   03 | 04 | 05   06   07 | 08   09
#    ------    -    -    ------    -    -
# 11   12 | 13   14   15   16 | 17   18 | 19
# ---------    -----------    -----------
# 21   22 | 23   24 | 25 | 26   27 | 28   29
#    -    ------    -    ------    ------
# 31 | 32   33 | 34   35 | 36   37   38 | 39
#    -    -----------    -----------    -
# 41   ST   43   44 | 45 | 46   47   48 | 49
#    -    -----------    -    -----------
# 51 | 52 | 53   54   55 | 56 | KEY| 58   59
# ----    -    -    -    -    -    -    -
# 61   62   63 | 64   65 | 66 | 67 | 68 | 69
# --------------LOCK------    -    -    ----
# 71  EXIT| 73   74 | 75   76   77 | 78   79
#    -----------    ------    -----------
# 81   82   83 | 84   85 | 86 | 87 | 88   89
#    ------    ------    -    -    ------
# 91   92 | 93   94   95 | 96 | 97   98   99


 elif run_maze_nr == 5:
  can_up = [11,13,14,15,17,18,19,23,26,29,31,32,34,35,37,39,42,45,48,49,51,52,55,56,59,62,63,64,65,66,67,68,69,74,76,77,78,81,84,86,89,91,93,95,96,97,99]
  can_down = [1,3,4,5,7,8,9,13,16,19,21,22,24,25,27,29,32,35,38,39,41,42,45,46,49,52,53,54,55,56,57,58,59,66,67,68,71,74,76,79,81,83,85,86,87,89]
  can_left = [2,3,6,7,9,12,14,15,16,18,22,24,27,29,33,35,37,38,42,43,44,47,48,54,55,59,62,63,65,72,74,76,77,79,82,83,85,89,92,94,95,98,99]
  can_right = [1,2,5,6,8,11,13,14,15,17,21,23,26,28,32,34,36,37,41,42,43,46,47,53,54,58,61,62,64,71,73,75,76,78,81,82,84,88,91,93,94,97,98]

  position = 42
  exit = 72
  key = 57  # zero for no key
  lock_pos = 64  # zero foɾ no key

  # Do *not* change
  inv_key = False
  lock_up = False
  lock_down = True
  lock_left = False
  lock_right = False

  clear()
  game()

# Maze 6

# 01 | 02   03 | 04  STRT|EXIT| 07 | 08   09
#    -    ------    -    -    -    ------
# 11 | 12   13 | 14 | 15 | 16   17   18   19
#    -    -    -    ---------------------
# 21 | 22 | 23   24 | 25   26 | 27   28   29
#    -    -    ------    ------    ---------
# 31   32 | 33   34 | 35 | 36   37   38   39
# ----    -----------    -    -----------
# 41   42 | 43   44   45 | 46 | KEY| 48   49
#    ------    -    ------    -    -    ----
# 51   52 | 53 | 54   55   56 | 57 | 58   59
#    ------    ----------------    -    ----
# 61   62 | 63   64   65   66   67 | 68 | 69
#    -    ------    -    -    ------    -
# 71 | 72   73   74 | 75 | 76 | 77   78 | 79
#LOCK--------------------------    ------
# 81 | 82   83   84   85 | 86 | 87   88   89
#    -    ------    ------    ------    -
# 91   92 | 93   94   95 | 96   97   98 | 99


 elif run_maze_nr == 6:
  can_up = [11,12,14,15,16,17,19,21,22,23,24,29,31,32,33,35,37,42,45,46,49,51,53,54,56,57,58,61,63,67,68,71,72,74,75,76,78,79,81,87,89,91,92,94,96,98,99]
  can_down = [1,2,4,5,6,7,9,11,12,13,13,14,19,21,22,23,25,27,32,35,36,39,41,43,44,46,47,48,51,53,57,58,61,62,64,65,66,68,69,77,79,81,82,86,88,89]
  can_left = [3,5,9,13,17,18,19,24,26,28,29,32,34,37,38,39,42,44,45,49,52,55,56,59,62,64,65,66,67,73,74,78,83,84,85,88,89,92,94,95,97,98]
  can_right = [2,4,8,12,16,17,18,23,25,27,28,31,33,36,37,38,41,43,44,48,51,54,55,58,61,63,64,65,66,72,73,77,82,83,84,87,88,91,93,94,96,97]

  position = 5
  exit = 6
  key = 47  # zero for no key
  lock_pos = 71  # zero foɾ no key

  # In which direction are the locked 'doors'
  lock_up = False
  lock_down = True
  lock_left = False
  lock_right = False

  # Do *not* change
  inv_key = False

  clear()
  game()

# debug

# 01 | 02 | 03 | 04 | 05
# ---------    ------
# 11 | 12   13   14 | 15
# ----    -    -    ----
# 21   22   23   24   25
# ----    -    -    ----
# 31 | 32   33   34 | 35
# ---------    ---------
# 41 | 42 | 43 | 44 | 45

 elif run_maze_nr == 70923081800910:
  can_up = [11,13,15,22,23,24,32,33,34,41,43,45]
  can_down = [1,3,5,12,13,14,22,23,24,31,33,35]
  can_left = [2,5,13,14,22,23,24,25,33,34,42,45]
  can_right = [1,4,12,13,21,22,23,24,32,33,41,44]

  position = int(input('position = '))
  exit = int(input('exit = '))
  key = int(input('key_pos = '))  # zero for no key
  lock_pos = int(input('lock_pos = '))  # zero foɾ no key
  # Do *not* change
  inv_key = False
  lock_up = False
  lock_down = False
  lock_left = False
  lock_right = False
  print(' 8 - lock_up = True\n 2 - lock_down = True\n 4 - lock_left = True\n 6 - lock_right = True\n anything else = everything false')
  debug_map_input = input('> ')
  if debug_map_input == '8':
   lock_up = True
  if debug_map_input == '2':
   lock_down = True
  if debug_map_input == '4':
   lock_left = True
  if debug_map_input == '6':
   lock_right = True

  clear()
  game()

# Maze 7

# 01   02   03 | 04   05   06 | 07   08   09
# ----    ------    ------    -    ------
# 11   12 | 13   14 | 15   16 | 17 | 18   19
#    ------    ------    ------    -    -
# 21   22   23   24 | 25   26 | 27 | 28 | 29
# ----    -    ------    ------    -    ----
# END  32 | 33   34 | 35   36   37 | 38   39
# -------------------LOCK-----------    ----
# 41   42 | 43   44 | 45 | 46   47 | 48 | 49
#    ------    -    -    ------    -    -
# 51   52   53 | 54 |STRT| 56   57 | 58   59
#    -----------    -    -    --------------
# 61 | 62   63   64 | 65 | 66   67   68   69
#    -----------    -    -    -----------
# 71 | 72   73 | 74 | 75 | 76 | 77   78 | 79
#    -    -    -    -    -    -    -    -
# 81 | 82 | 83   84   85   86   87 | 88 | 89
#    -    --------------------------    -
# 91 | 92   93   94  K E Y 96   97   98 | 99


 elif run_maze_nr == 7:
  can_up = [12,14,16,17,19,21,23,25,27,28,29,32,33,35,37,38,48,51,53,54,55,57,58,59,61,64,65,66,71,74,75,76,79,81,82,83,84,85,86,87,88,89,91,92,98,99]
  can_down = [2,4,6,7,9,11,13,15,17,18,19,22,23,25,27,28,35,38,41,43,44,45,47,48,49,51,54,55,56,61,64,65,66,69,71,72,73,74,75,76,77,78,79,81,82,88,89]
  can_left = [2,3,5,6,8,9,12,14,16,19,22,23,24,26,32,34,36,37,39,42,44,47,52,53,57,59,63,64,67,68,69,73,78,84,85,86,87,93,94,95,96,97,98]
  can_right = [1,2,4,5,7,8,11,13,15,18,21,22,23,25,31,33,35,36,38,41,43,46,51,52,56,58,62,63,66,67,68,72,77,83,84,85,86,92,93,94,95,96,97]

  position = 55
  exit = 31
  key = 95  # zero for no key
  lock_pos = 45  # zero foɾ no key
  # Do *not* change
  inv_key = False
  lock_up = True
  lock_down = False
  lock_left = False
  lock_right = False

  clear()
  game()

# Maze 8

# 01   02   03   04   05   06   07   08   09
#    ------------------------------------
# 11 | 12   13   14 | 15   16   17   18 | 19
#    -----------    -    -    -    ------
# 21 | 22   23   24 | 25 | 26 | 27   28 | 29
#    -    -    -----------    ------    -
# 31 | 32 | 33 |EXIT  35 | 36 | 37 | 38 | 39
#    -    -    ------    -    -    -    -
# 41 | 42 | 43   44 | 45   46 | 47   48 | 49
#    -----------    -----------    -    -
# 51 | 52   53   54 | 55   56   57 | 58 | 59
#    -    -----------    ----------------
# 61 | 62 | 63   64   65 | 66   67   68 | 69
#    -    -    ------    -    ------    -
# 71 | 72   73 | 74   75 | 76  KEY | 78 |MSG1
#    ------    -    ----------------    ----
# 81 | 82   83 | 84   85   86   87   88   89
#    ------------------------------------
# 91   92   93   94   95   96   97   98 L 99


 elif run_maze_nr == 8:
  can_up = [11,19,21,24,25,26,27,29,31,32,33,36,38,39,41,42,43,45,46,47,48,49,51,54,57,58,59,61,62,65,69,71,72,73,75,76,78,81,83,84,88,91,99]
  can_down = [1,9,11,14,15,16,17,19,21,22,23,26,28,29,31,32,33,35,36,37,38,39,41,44,47,48,49,51,52,55,59,61,62,63,65,66,68,69,71,73,74,78,81,89]
  can_left = [2,3,4,5,6,7,8,9,13,14,16,17,18,23,24,28,35,44,46,48,53,54,56,57,64,65,67,68,73,75,77,83,85,86,87,88,89,92,93,94,95,96,97,98]
  can_right = [1,2,3,4,5,6,7,8,12,13,15,16,17,22,23,27,34,43,45,47,52,53,55,56,63,64,66,67,72,74,76,82,84,85,86,87,88,91,92,93,94,95,96,97,98]

  position = 88
  exit = 34
  key = 77  # zero for no key
  lock_pos = 99  # zero foɾ no key
  msg1_pos = 79
  msg1 = 'A máme chyceného blbečka'
  # Do *not* change
  inv_key = False
  lock_up = False
  lock_down = False
  lock_left = True
  lock_right = False

  clear()
  game()