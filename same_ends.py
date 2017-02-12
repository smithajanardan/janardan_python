
#  File: same_ends.py 

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Given a string, return the longest substring 
# that appears at both the beginning and end of 
# the string without overlapping. For example, 
# same_ends("abXab") is "ab".

# same_ends("abXYab") -> "ab"
# same_ends("xx") -> "x"
# same_ends("xxx") -> "x"

def same_ends(str):
  # WRITE YOUR CODE HERE


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
    ["ab", "abXYab"],
    ["x", "xx"],
    ["x", "xxx"],
    ["xx", "xxxx"],
    ["python", "pythonXYZpython"],
    ["python", "pythonpython"],
    ["", "xythonXYZpython"],
    ["", "x"],
    ["", ""],
    ["", "abcb"],
    ["my", "mymmy"]]

  count = 0
  total = len(args)
  for arg in args:
    result = same_ends(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "same_ends", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()
