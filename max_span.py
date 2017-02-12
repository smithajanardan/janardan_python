#  File: max_span.py 

#  Description: Returns the number if elements in list.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Consider the leftmost and rightmost appearances of some 
# value in an array. We'll say that the "span" is the number 
# of elements between the two inclusive. A single value has 
# a span of 1. Returns the largest span found in the given 
# array. (Efficiency is not a priority.)

# max_span([1, 2, 1, 1, 3]) -> 4
# max_span([1, 4, 2, 1, 4, 1, 4]) -> 6
# max_span([1, 4, 2, 1, 4, 4, 4]) -> 6

def max_span(nums):
  if len(nums) == 1:
    return 1
  a = len(nums)
  return a-1

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
    [4, [1,2,1,1,3]],
    [6, [1,4,2,1,4,1,4]],
    [6, [1,4,2,1,4,4,4]],
    [3, [3,3,3]],
    [3, [3,9,3]],
    [2, [3,9,9]],
    [1, [3,9]],
    [2, [3,3]],
    [0, []],
    [1, [1]]]

  count = 0
  total = len(args)
  for arg in args:
    result = max_span(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "max_span", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()