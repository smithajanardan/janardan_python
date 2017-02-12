#  File: max_block.py 

#  Description: Returns length of largest same number sequence.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given a string, return the length of the largest 
# "block" in the string. A block is a run of adjacent 
# chars that are the same.

# max_block("hoopla") -> 2
# max_block("abbCCCddBBBxx") -> 3
# max_block("") -> 0

def max_block(str):
  b = list(str)
  idx = b[0]
  count = 0
  if len(b) == 0:
    return count
  for i in range(len(b)-1):
    idx = list.index(b[i], idx)    
    idx2 = list.index(b[i], idx)
    count2 = idx2-idx
    if count2 > count:
      count = count2
  return count

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
    [2, "hoopla"],
    [3, "abbCCCddBBBxx"],
    [0, ""],
    [1, "xyz"],
    [2, "xxyz"],
    [2, "xyzz"],
    [3, "abbbcbbbxbbbx"],
    [3, "XXBBBbbxx"],
    [4, "XXXBBBBbbxx"],
    [4, "XXBBBbbxxXXXX"],
    [4, "XX2222BBBbbXX2222"]]

  count = 0
  total = len(args)
  for arg in args:
    result = max_block(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "max_block", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()