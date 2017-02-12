#  File: can_balance.py 

#  Description: Splits a list into two equal value parts.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Given a non-empty array, return True if there is a place 

# to split the array so that the sum of the numbers on one 

# side is equal to the sum of the numbers on the other side.



# can_balance([1, 1, 1, 2, 1]) -> True

# can_balance([2, 1, 1, 2, 1]) -> False

# can_balance([10, 10]) -> True



def can_balance(nums):

  sum = 0
  for item in nums:
    sum = sum + item 
  partial_sum = 0
  for idx in nums:
    partial_sum = partial_sum + idx
    if (partial_sum) == (sum-partial_sum):
      return True
  return False    


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

    [True, [1,1,1,2,1]],

    [False, [2,1,1,2,1]],

    [True, [10,10]],

    [True, [10,0,1,-1,10]],

    [True, [1,1,1,1,4]],

    [False, [2,1,1,1,4]],

    [False, [2,3,4,1,2]],

    [True, [1,2,3,1,0,2,3]],

    [False, [1,2,3,1,0,1,3]],

    [False, [1]],

    [True, [1,1,1,2,1]]]



  count = 0

  total = len(args)

  for arg in args:

    result = can_balance(arg[1])

    is_correct = result == arg[0]

    if is_correct:

      count += 1

    print showMessage(is_correct, "can_balance", arg, result)

  if count == total:

    print "All Correct!"

  else:
    print "passed " + str(count) + " out of " + str(total)



main()
