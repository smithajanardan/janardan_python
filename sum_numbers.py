#  File: sum_numbers.py 

#  Description: Returns the sum of each sequence.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given a string, return the sum of the numbers appearing 
# in the string, ignoring all other characters. A number 
# is a series of 1 or more digit chars in a row. (Note: 
# s.isdigit() returns if all the characters in s are digits. 
# int(s) coverts a string to an int)

# sum_numbers("abc123xyz") -> 123
# sum_numbers("aa11b33") -> 44
# sum_numbers("7 11") -> 18

import string

def sum_numbers(str):
  s = ""
  for i in str:
    if not i.isdigit():
      s = s + i.replace(i," ")
    else:
      s = s + i
  s = s.split()
  sum = 0
  for j in s:
    sum += int(j)
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
    [123, "abc123xyz"],
    [44, "aa11b33"],
    [18, "7 11"],
    [0, "Chocolate"],
    [7, "5hoco1a1e"],
    [7, "5##1;;1!!"],
    [1245, "a1234bb11"],
    [0, ""],
    [25, "a22bbb3"]]

  count = 0
  total = len(args)
  for arg in args:
    result = sum_numbers(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "sum_numbers", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()