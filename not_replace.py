
#  File: not_replace.py 

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Given a string, return a string where every appearance 
# of the lowercase word "is" has been replaced with "is not". 
# The word "is" should not be immediately preceeded or followed 
# by a letter -- so for example the "is" in "this" does not 
# count. (Note: char.isalpha() tests if a char is a letter.)

# not_replace("is test") -> "is not test"
# not_replace("is-is") -> "is not-is not"
# not_replace("This is right") -> "This is not right"

def not_replace(str):
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
    ["is not test", "is test"],
    ["is not-is not", "is-is"],
    ["This is not right", "This is right"],
    ["This is not Isabell", "This is Isabell"],
    ["", ""],
    ["is not", "is"],
    ["isis", "isis"],
    ["Dis is not bliss is not", "Dis is bliss is"],
    ["is not his", "is his"],
    ["xis yis", "xis yis"],
    ["AAAis is not", "AAAis is"]]

  count = 0
  total = len(args)
  for arg in args:
    result = not_replace(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "not_replace", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()
