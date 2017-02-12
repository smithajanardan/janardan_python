#  File: square_up.py 

#  Description: Returns a triangle of factorial elements and elements of factorial elements.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given n>=0, create an array length n*n with the 
# following pattern, shown here for n=3 : 
# [0, 0, 1,    0, 2, 1,    3, 2, 1] 
# (spaces added to show the 3 groups).

# square_up(3) -> [0, 0, 1, 0, 2, 1, 3, 2, 1]
# square_up(2) -> [0, 1, 2, 1]
# square_up(4) -> [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]

def square_up(n):
  a = []
  c = 0
  e = n
  while e > 0:
    d = e
    b = []
    while d > 0:
      b.append(d)
      d = d-1
    f = len(b)
    while f < n:
      b.insert(0,0)
      f = len(b)
    a.append(b)
    e = e-1
  a.reverse()
  g = []
  for i in range(len(a)):
    for j in range(len(a)):
      g.append(a[i][j])
  return g

####################################################
###### DO NOT Modify anything below this line ######
####################################################

# Shows an argument. If arg is a string, add a pair of quotation to it.
def showArg(arg):
  type_arg = type(arg)
  result = ""
  if (type_arg == type(str())):
    result = '\"' + arg + '\"'
  else:
    result = str(arg)
  return result

# Shows a function call, including the name and all the arguments of a function.
def showFuncCall(name, args):
  result = name + '('
  for arg in args:
    result += showArg(arg)
    result += ", "
  if len(args) != 0:
    result = result[:-2]
  result += ')'
  return result

# Shows a message of a test sample.
def showMessage(is_correct, name, args, res):
  result = ""
  if is_correct:
    result += "Correct! "
    result += showFuncCall(name, args[1:])
    result += " = "
    result += showArg(args[0])
  else:
    result += "Wrong! "
    result += showFuncCall(name, args[1:])
    result += "\texpected: "
    result += showArg(args[0])
    result += "\tyour result: "
    result += showArg(res)
  return result


def main():
  args = [
    [[0,0,1,0,2,1,3,2,1], 3],
    [[0,1,2,1], 2],
    [[0,0,0,1,0,0,2,1,0,3,2,1,4,3,2,1], 4],
    [[1], 1],
    [[], 0],
    [[0,0,0,0,0,1,0,0,0,0,2,1,0,0,0,3,2,1,0,0,4,3,2,1,0,5,4,3,2,1,6,5,4,3,2,1], 6]]

  count = 0
  total = len(args)
  for arg in args:
    result = square_up(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "square_up", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()