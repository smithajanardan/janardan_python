#  File: sum_digits.py 

#  Description: Returns the sum of all digits in a string.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given a string, return the sum of the digits 0-9 
# that appear in the string, ignoring all other 
# characters. Return 0 if there are no digits in 
# the string. (Note: s.isdigit() returns if all the 
# characters in s are digits. int(s) coverts a string 
# to an int)

# sum_digits("aa1bc2d3") -> 6
# sum_digits("aa11b33") -> 8
# sum_digits("Chocolate") -> 0

def sum_digits(str):
  sum = 0
  for i in str:
    if i.isdigit():
      sum += int(i)
  return sum

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
    [6, "aa1bc2d3"],
    [8, "aa11b33"],
    [0, "Chocolate"],
    [7, "5hoco1a1e"],
    [12, "123abc123"],
    [0, ""],
    [0, "Hello World"],
    [12, "X1z9b2"],
    [14, "5432a"]]

  count = 0
  total = len(args)
  for arg in args:
    result = sum_digits(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "sum_digits", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()