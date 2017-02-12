#  File: max_mirror.py 

#  Description: Returns the length of the largest mirrored subsequence.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Say that a "mirror" section in an array is a group of 
# contiguous elements such that somewhere in the array, 
# the same group appears in reverse order. For example, 
# the largest mirror section in [1, 2, 3, 8, 9, 3, 2, 1] 
# is length 3 (the [1, 2, 3] part). Return the size of 
# the largest mirror section found in the given array.

# max_mirror([1, 2, 3, 8, 9, 3, 2, 1]) -> 3
# max_mirror([1, 2, 1, 4]) -> 3
# max_mirror([7, 1, 2, 9, 7, 2, 1]) -> 2

def max_mirror(nums):
  

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
    [3, [1,2,3,8,9,3,2,1]],
    [3, [1,2,1,4]],
    [2, [7,1,2,9,7,2,1]],
    [4, [21,22,9,8,7,6,23,24,6,7,8,9,25,7,8,9]],
    [4, [1,2,1,20,21,1,2,1,2,23,24,2,1,2,1,25]],
    [5, [1,2,3,2,1]],
    [2, [1,2,3,3,8]],
    [2, [1,2,7,8,1,7,2]],
    [3, [1,1,1]]]

  count = 0
  total = len(args)
  for arg in args:
    result = max_mirror(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "max_mirror", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()