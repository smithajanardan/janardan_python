#  File: linear_in.py 

#  Description: Verifies if one list is inside of another list.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given two arrays of ints sorted in increasing order, 
# outer and inner, return True if all of the numbers 
# in inner appear in outer. The best solution makes 
# only a single "linear" pass of both arrays, taking 
# advantage of the fact that both arrays are already 
# in sorted order.

# linear_in([1, 2, 4, 6], [2, 4]) -> True
# linear_in([1, 2, 4, 6], [2, 3, 4]) -> False
# linear_in([1, 2, 4, 4, 6], [2, 4]) -> True

def linear_in(outer, inner):
  for item in inner:
    if not item in outer:
      return False
  return True

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
    [True, [1,2,4,6], [2,4]],
    [False, [1,2,4,6], [2,3,4]],
    [True, [1,2,4,4,6], [2,4]],
    [True, [2,2,4,4,6,6], [2,4]],
    [True, [2,2,2,2,2], [2,2]],
    [False, [2,2,2,2,2], [2,4]],
    [True, [2,2,2,2,4], [2,4]],
    [True, [1,2,3], [2]],
    [False, [1,2,3], [-1]],
    [True, [1,2,3], []],
    [True, [-1,0,3,3,3,10,12], [-1,0,3,12]],
    [False, [-1,0,3,3,3,10,12], [0,3,12,14]],
    [False, [-1,0,3,3,3,10,12], [-1,10,11]]]

  count = 0
  total = len(args)
  for arg in args:
    result = linear_in(arg[1], arg[2])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "linear_in", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()