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
 print('[Warning] Without "os" module the game might start be laggy after some time on low-end devices')
 print('[Tip] Reboot your terminal emulator after every level')
 input('Press "Enter" to continue or Ctrl+C to exit')
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
debug_show_pos = False
key = 0
lock = 0
xxx = 0
msg1 = ''
msg1_pos = 0
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
 print('\n\n          _____________________________________             _____________')
 print('         /#####################################            / MrBurgerCZ /')
 print('        /#                                  /#            /"""""""""""""')
 print('       /#  mail       mrburgercz@gmail.com /#       _..--/-.._')
 print('      /#  GitHub     MrBurgerCZ           /#       /__,_______\ ')
 print('     /#  reddit     u/MrBurgerCZ         /#       (_,______,___)')
 print('    /#  Discord    @mrburgercz          /#        (,,,,,,,,,,,,)')
 print('   /#  Instagram  @mrburgercz          /#         (__, ,__/|_,_)')
 print('  /#__________________________________/#           \_!`\______/')
 print(' /#####################################        \n')

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
  print('       Thank you for playing my game!\n\n\n\n')
  print('             _____________')
  print('            / MrBurgerCZ /')
  print('           /"""""""""""""')
  print('     _..--/-.._')
  print('    /__,_______\ ')
  print('   (_,______,___)')
  print('   (,,,,,,,,,,,,)')
  print('   (__, ,__/|_,_)')
  print('    \_!`\______/ \n\n\n')
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

  can_up = [101,103,104,201,203,204,301,302,303]
  can_down = [1,3,4,101,103,104,201,202,203]
  can_left = [2,3,102,104,303,304]
  can_right = [1,2,101,103,302,303]

  position = 2
  exit = 202
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

  can_up = [101,102,104,105,201,205,206,302,306,401,403,404,405,406]
  can_down = [1,2,4,5,101,105,106,202,206,301,303,304,305,306]
  can_left = [4,5,6,102,103,104,203,204,205,206,303,402,403,405,406]
  can_right = [3,4,5,101,102,103,202,203,204,205,302,401,402,404,405]

  position = 305
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

  can_up = [101,102,104,106,108,109,203,204,206,207,208,209,301,302,306,308,401,403,404,407,501,503,504,505,506,508,509,601,603,606,608,609,701,704,707,709,803,804,806,808]
  can_down = [1,2,4,6,8,9,103,104,106,107,108,109,201,202,206,208,301,303,304,307,401,403,404,405,406,408,409,501,503,506,508,509,601,604,607,609,703,704,706,708]
  can_left = [3,4,5,7,8,9,105,106,202,204,205,207,303,304,306,308,402,406,407,503,505,506,507,603,606,607,608,702,703,705,706,709,802,803,804,805,807,808]
  can_right = [2,3,4,6,7,8,104,105,201,203,204,206,302,303,305,307,401,405,406,502,504,505,506,602,605,606,607,701,702,704,705,708,801,802,803,804,806,807]

  position = 107
  exit = 409
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
  can_up = [101,102,103,105,109,201,202,203,205,206,208,209,302,307,308,309,401,403,404,405,406,407,409,501,502,504,506,507,509,601,602,604,606,609,701,705,706,707,709,801,803,804,807,808,809]
  can_down = [1,2,3,5,9,101,102,103,105,106,108,109,202,207,208,209,301,303,304,305,306,307,309,401,404,406,407,409,501,502,504,506,509,601,605,606,607,609,701,703,704,707,708,709]
  can_left = [3,4,6,7,8,9,105,107,108,202,204,205,206,209,302,303,306,308,403,405,409,503,504,506,509,603,609,702,705,708,802,803,804,805,806,807,809]
  can_right = [2,3,5,6,7,8,104,106,107,201,203,204,205,208,301,302,305,307,402,404,408,502,503,505,508,602,608,701,704,707,801,802,803,804,805,806,808]

  position = 3
  exit = 706
  key = 508
  lock_pos = 402
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
  can_up = [101,103,104,105,107,108,109,203,206,209,301,302,304,305,307,309,402,405,408,409,501,502,505,506,509,602,603,604,605,606,607,608,609,704,706,707,708,801,804,806,809,901,903,905,906,907,909]
  can_down = [1,3,4,5,7,8,9,103,106,109,201,202,204,205,207,209,302,305,308,309,401,402,405,406,409,502,503,504,505,506,507,508,509,606,607,608,701,704,706,709,801,803,805,806,807,809]
  can_left = [2,3,6,7,9,102,104,105,106,108,202,204,207,209,303,305,307,3080,402,403,404,407,408,504,505,509,602,603,605,702,704,706,707,709,802,803,805,809,902,904,905,908,909]
  can_right = [1,2,5,6,8,101,103,104,105,107,201,203,206,208,302,304,306,307,401,402,403,406,407,503,504,508,601,602,604,701,703,705,706,708,801,802,804,808,901,903,904,907,908]

  position = 402
  exit = 702
  key = 507  # zero for no key
  lock_pos = 604  # zero foɾ no key

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
  can_up = [101,102,104,105,106,107,109,201,202,203,204,209,301,302,303,305,307,402,405,406,409,501,503,504,506,507,508,601,603,607,608,701,702,704,705,706,708,709,801,807,809,901,902,904,906,908,909]
  can_down = [1,2,4,5,6,7,9,101,102,103,103,104,109,201,202,203,205,207,302,305,306,309,401,403,404,406,407,408,501,503,507,508,601,602,604,605,606,608,609,707,709,801,802,806,808,809]
  can_left = [3,5,9,103,107,108,109,204,206,208,209,302,304,307,308,309,402,404,405,409,502,505,506,509,602,604,605,606,607,703,704,708,803,804,805,808,809,902,904,905,907,908]
  can_right = [2,4,8,102,106,107,108,203,205,207,208,301,303,306,307,308,401,403,404,408,501,504,505,508,601,603,604,605,606,702,703,707,802,803,804,807,808,901,903,904,906,907]

  position = 5
  exit = 6
  key = 407  # zero for no key
  lock_pos = 701  # zero foɾ no key

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

# 001 | 002 | 003 | 004 | 005
# -----------     -----------
# 101 | 102   103   104 | 105
# -----     -     -     -----
# 201   202   203   204   205
# -----     -     -     -----
# 301 | 302   303   304 | 305
# -----------     -----------
# 401 | 402 | 403 | 404 | 405

 elif run_maze_nr == 70923081800910:
  can_up = [101,103,105,202,203,204,302,303,304,401,403,405]
  can_down = [1,3,5,102,103,104,202,203,204,301,303,305]
  can_left = [2,5,103,104,202,203,204,205,303,304,402,405]
  can_right = [1,4,102,103,201,202,203,204,302,303,401,404]

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
  can_up = [102,104,106,107,109,201,203,205,207,208,209,302,303,305,307,308,408,501,503,504,505,507,508,509,601,604,605,606,701,704,705,706,709,801,802,803,804,805,806,807,808,809,901,902,908,909]
  can_down = [2,4,6,7,9,101,103,105,107,108,109,202,203,205,207,208,305,308,401,403,404,405,407,408,409,501,504,505,506,601,604,605,606,609,701,702,703,704,705,706,707,708,709,801,802,808,809]
  can_left = [2,3,5,6,8,9,102,104,106,109,202,203,204,206,302,304,306,307,309,402,404,407,502,503,507,509,603,604,607,608,609,703,708,804,805,806,807,903,904,905,906,907,908]
  can_right = [1,2,4,5,7,8,101,103,105,108,201,202,203,205,301,303,305,306,308,401,403,406,501,502,506,508,602,603,606,607,608,702,707,803,804,805,806,902,903,904,905,906,907]

  position = 505
  exit = 301
  key = 905  # zero for no key
  lock_pos = 405  # zero foɾ no key
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
#    -    -    ------    -    ------    --vv--
# 71 | 72   73 | 74   75 | 76  KEY | 78 |MSG1
#    ------    -    ----------------    ------
# 81 | 82   83 | 84   85   86   87   88   89
#    ------------------------------------
# 91   92   93   94   95   96   97   98 L 99


 elif run_maze_nr == 8:
  can_up = [101,109,201,204,205,206,207,209,301,302,303,306,308,309,401,402,403,405,406,407,408,409,501,504,507,508,509,601,602,605,609,701,702,703,705,706,708,801,803,804,808,901,909]
  can_down = [1,9,101,104,105,106,107,109,201,202,203,206,208,209,301,302,303,305,306,307,308,309,401,404,407,408,409,501,502,505,509,601,602,603,605,606,608,609,701,703,704,708,801,809]
  can_left = [2,3,4,5,6,7,8,9,103,104,106,107,108,203,204,208,305,404,406,408,503,504,506,507,604,605,607,608,703,705,707,803,805,806,807,808,809,902,903,904,905,906,907,908]
  can_right = [1,2,3,4,5,6,7,8,102,103,105,106,107,202,203,207,304,403,405,407,502,503,505,506,603,604,606,607,702,704,706,802,804,805,806,807,808,901,902,903,904,905,906,907,908]

  position = 808
  exit = 304
  key = 707  # zero for no key
  lock_pos = 909  # zero foɾ no key
  msg1_pos = 709
  msg1 = 'A máme chyceného blbečka'
  # Do *not* change
  inv_key = False
  lock_up = False
  lock_down = False
  lock_left = True
  lock_right = False

  clear()
  game()

# Maze 9

#   001| 002| 003| 004| 005| 006| 007| 008| 009| 010| 011| 012
# -------------------------------------------------------------
#   101| 102| 103| 104| 105| 106| 107| 108| 109| 110| 111| 112
# -------------------------------------------------------------
#   201| 202| 203| 204| 205| 206| 207| 208| 209| 210| 211| 212
# -------------------------------------------------------------
#   301| 302| 303| 304| 305| 306| 307| 308| 309| 310| 311| 312
# -------------------------------------------------------------
#   401| 402| 403| 404| 405| 406| 407| 408| 409| 410| 411| 412
# -------------------------------------------------------------
#   501| 502| 503| 504| 505| 506| 507| 508| 509| 510| 511| 512
# -------------------------------------------------------------
#   601| 602| 603| 604| 605| 606| 607| 608| 609| 610| 611| 612
# -------------------------------------------------------------
#   701| 702| 703| 704| 705| 706| 707| 708| 709| 710| 711| 712
# -------------------------------------------------------------
#   801| 802| 803| 804| 805| 806| 807| 808| 809| 810| 811| 812
# ----------------    -----------------------------------------
#   901| 902| 903| 904| 905| 906| 907| 908| 909| 910| 911| 912
# ----------------    -----------------------------------------
#  1001 1002 1003 STRT 1005 1006|1007|1008|1009|1010|1011|1012
# -    -----------    -----------------------------------------
#  1101|1102 1103|1104|1105|1106|1107|1108|1109|1110|1111|1112
# -    -    ------    -----------------------------------------
#  1201 1202 1203|1204|1205|1206|1207|1208|1209|1210|1211|1212

 elif run_maze_nr == 9:
  can_up = []
  can_down = []
  can_left = []
  can_right = []

  position = 0
  exit = 0
  key = 0  #   zero for no key
  lock_pos = 0  #   zero foɾ no key
  #   Do *not* change
  inv_key = False
  lock_up = False
  lock_down = True
  lock_left = False
  lock_right = False

  clear()
  game()
