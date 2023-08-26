### BurgerMaze - game by MrBurgerCZ (c) 2023 ###

## First, we will import needed libraries
import os, time, random

## Then, we will make some actions easier to do
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
 print('  Quit = "exit"')
 if show_error:
  print('Input does have to be one of these inputs: "2","4","6","8", or "exit".')
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
key = 0
lock = 0
s = os.get_terminal_size()
l = s.lines

def game():
 global position, goto, key, lock_pos, inv_key, prefix
 global lock_up, lock_down, lock_left, lock_right
 game_input = 42
 while(True):
  prefix = ''
  if position == exit:
   maze_icon()
   print('\n#########################\n# You found the Exit!!! #\n#########################\n')
   break
  if position == key:
   inv_key = True
   prefix = 'You found the key!'
  if position == lock_pos:
   if inv_key:
    lock()
   else:
    prefix = 'You must have a key to unlock this lock!'
  maze_icon()
  print_move()
  game_input = input('\n>>> ')
  if game_input == 'exit':
   break
  try:
   goto = int(game_input)
  except:
   print('Input does have to be one of these inputs: "2","4","6","8", or "exit".')
  position = move()

def maze_icon():
 global prefix
 space='       '
 if contains(can_up,position) == False:
  line_a = '---------'
 else:
  line_a = '-       -'
 if contains(can_left,position) == False:
  line_b = '|'
 else:
  line_b = ' '
 if contains(can_right,position) == False:
  line_c = '|'
 else:
  line_c = ' '
 if contains(can_down,position) == False:
  line_d = '---------'
 else:
  line_d = '-       -'
 global l
 clear()
 for i in range(l - 13):
  print()
 print(f' {prefix}\n\n {line_a}\n {line_b}{space}{line_c}\n {line_b}{space}{line_c}\n {line_b}{space}{line_c}\n {line_d}')

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
clear()
print()
print('  ############################################')
print('  # BurgerMaze - game by MrBurgerCZ (c) 2023 #')
print('  ############################################')
print()
quit = False
while(True):
 if quit:
  print('Thank you for playing my game!')
  break

# Level picker
 run_maze = 0
 while(True):
  global lock_pos
  print('Higher level number means higher difficulty.\n\nChoose a level:\n Level 1\n Level 2\n Level 3\n Level 4\n\nType "exit" to quit.')
  run_maze = input('> ')
  try:
   run_maze_nr = int(run_maze)
  except:
   run_maze_nr = 0
  if run_maze_nr != 0:
   break
  if run_maze == 'exit':
   quit = True
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
