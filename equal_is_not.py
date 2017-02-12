
#  File: equal_is_not.py 

#  Description: Verifies the appearance of "is" equals the appearance of "not"

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given a string, return true if the number of 

# appearances of "is" anywhere in the string is 

# equal to the number of appearances of "not" 

# anywhere in the string (case sensitive).



# equal_is_not("This is not") -> false

# equal_is_not("This is notnot") -> true

# equal_is_not("noisxxnotyynotxisi") -> true


import string


def equal_is_not(str):

  count_is = str.count("is")
  count_not = str.count("not")
  return count_is == count_not



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

    [False, "This is not"],

    [True, "This is notnot"],

    [True, "noisxxnotyynotxisi"],

    [False, "noisxxnotyynotxsi"],

    [True, "xxxyyyzzzintint"],

    [True, ""],

    [True, "isisnotnot"],

    [False, "isisnotno7Not"],

    [False, "isnotis"],

    [False, "mis3notpotbotis"]]



  count = 0

  total = len(args)

  for arg in args:

    result = equal_is_not(arg[1])

    is_correct = result == arg[0]

    if is_correct:

      count += 1

    print showMessage(is_correct, "equal_is_not", arg, result)

  if count == total:

    print "All Correct!"

  else:

    print "passed " + str(count) + " out of " + str(total)



main()