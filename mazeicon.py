def contains(ca,cb):
 return list.__contains__(ca,cb)

can_up = [11,13,14,21,23,24,31,32,33]
can_down = [1,3,4,11,13,14,21,22,23]
can_left = [2,3,12,14,33,34]
can_right = [1,2,11,13,32,33]

inuuu = int(input())
position = inuuu

prefix = 'Hello there.'

def maze():
 global prefix
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
  line_Ca = '---------'
 else:
  line_Ca = '-       -'
 if contains(can_left,position) == False:
  line_Cb = '|'
 else:
  line_Cb = ' '
 if contains(can_right,position) == False:
  line_Cc = '|'
 else:
  line_Cc = ' '
 if contains(can_down,position) == False:
  line_Cd = '---------'
 else:
  line_Cd = '-       -'

 print(f' {prefix}\n\n {line_Ub}{space}{line_Uc}\n {line_La}{line_Ca}{line_Ra}\n   {line_Cb}{space}{line_Cc}\n   {line_Cb}  You  {line_Cc}\n   {line_Cb}{space}{line_Cc}\n {line_Ld}{line_Cd}{line_Rd}\n {line_Db}{space}{line_Dc}')

#print(f' {prefix}\n\n {line_a}\n {line_b}{space}{line_c}\n {line_b}{space}{line_c}\n {line_b}{space}{line_c}\n {line_d}')

maze()