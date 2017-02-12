#  File: without_string.py 

#  Description: Removes all occurances of the substring in string.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given two strings, base and remove, return a version 
# of the base string where all instances of the remove 
# string have been removed (not case sensitive). You 
# may assume that the remove string is length 1 or more. 
# Remove only non-overlapping instances, so with "xxx" 
# removing "xx" leaves "x".

# without_string("Hello there", "llo") -> "He there"
# without_string("Hello there", "e") -> "Hllo thr"
# without_string("Hello there", "x") -> "Hello there"

def without_string(base, remove):
  remove = remove.lower()
  idx = base.find(remove)
  while idx >= 0:
    base = base.replace(remove, "")
    idx = base.find(remove)
  remove = remove.upper()
  idx = base.find(remove)
  while idx >= 0:
    base = base.replace(remove, "")
    idx = base.find(remove)
  return base

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
    ["He there", "Hello there", "llo"],
    ["Hllo thr", "Hello there", "e"],
    ["Hello there", "Hello there", "x"],
    ["Th  a FH", "This is a FISH", "IS"],
    ["TH  a FH", "THIS is a FISH", "is"],
    ["TH  a FH", "THIS is a FISH", "iS"],
    ["abab", "abxxxxab", "xx"],
    ["abxab", "abxxxab", "xx"],
    ["", "xxx", "x"],
    ["x", "xxx", "xx"],
    ["xzz", "xyzzy", "Y"],
    ["", "", "x"],
    ["acac", "abcabc", "b"]]

  count = 0
  total = len(args)
  for arg in args:
    result = without_string(arg[1], arg[2])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "without_string", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()