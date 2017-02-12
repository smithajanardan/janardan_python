#  File: series_up.py 

#  Description: Returns the factorial elements a number and each element's facotrial elements.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given n>=0, create an array with the pattern 
# [1,    1, 2,    1, 2, 3,   ... 1, 2, 3 .. n] 
# (spaces added to show the grouping). Note that 
# the length of the array will be 1 + 2 + 3 ... + n, 
# which is known to sum to exactly n*(n + 1)/2.

# series_up(3) -> [1, 1, 2, 1, 2, 3]
# series_up(4) -> [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]
# series_up(2) -> [1, 1, 2]

import string

def series_up(n):
  str = []
  while n > 0:
    b = n
    while b > 0:
      str.append(b)
      b = b - 1
    n = n - 1
  str.reverse()
  return str

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
    [[1,1,2,1,2,3], 3],
    [[1,1,2,1,2,3,1,2,3,4], 4],
    [[1,1,2], 2],
    [[1], 1],
    [[], 0],
    [[1,1,2,1,2,3,1,2,3,4,1,2,3,4,5,1,2,3,4,5,6], 6]]

  count = 0
  total = len(args)
  for arg in args:
    result = series_up(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "series_up", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()