
#  File: mirror_ends.py 

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Given a string, look for a mirror image (backwards) 
# string at both the beginning and end of the given 
# string. In other words, zero or more characters at 
# the very begining of the given string, and at the 
# very end of the string in reverse order (possibly 
# overlapping). For example, the string "abXYZba" has 
# the mirror end "ab".

# mirror_ends("abXYZba") -> "ab"
# mirror_ends("abca") -> "a"
# mirror_ends("aba") -> "aba"

def mirror_ends(str):
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
    ["ab", "abXYZba"],
    ["a", "abca"],
    ["aba", "aba"],
    ["", "abab"],
    ["xxx", "xxx"],
    ["xxYxx", "xxYxx"],
    ["Hi ", "Hi and iH"],
    ["x", "x"],
    ["", ""],
    ["123", "123andthen 321"],
    ["ba", "band and ab"]]

  count = 0
  total = len(args)
  for arg in args:
    result = mirror_ends(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "mirror_ends", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()
