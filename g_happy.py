#  File: g_happy.py 

#  Description: Verifies that each g is in a pair.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# We'll say that a lowercase 'g' in a string 
# is "happy" if there is another 'g' immediately 
# to its left or right. Return true if all the g's 
# in the given string are happy.

# g_happy("xxggxx") -> true
# g_happy("xxgxx") -> false
# g_happy("xxggyygxx") -> false

def g_happy(str):
  if len(str) == 1:
    return False
  if len(str) == 0:
    return True
  prev = ""
  true = False
  for i in range(0,len(str)-1):
    if (str[i] == "g"):
      if prev == "g" or str[i+1] == "g":
        true = True
      else:
        return False
    prev = str[i]
  if str[len(str)-1] == "g" and str[len(str)-2] != "g":
    return False
  return true

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
    [True, "xxggxx"],
    [False, "xxgxx"],
    [False, "xxggyygxx"],
    [False, "g"],
    [True, "gg"],
    [True, ""],
    [True, "xxgggxyz"],
    [False, "xxgggxyg"],
    [True, "xxgggxygg"],
    [False, "gxyggxyz"],
    [False, "mgm"],
    [True, "mggm"],
    [True, "yyygggxyy"]]

  count = 0
  total = len(args)
  for arg in args:
    result = g_happy(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "g_happy", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()