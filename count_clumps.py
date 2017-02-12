#  File: count_clumps.py 

#  Description: Returns the number of same-number sequences

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# Say that a "clump" in an array is a series of 2 

# or more adjacent elements of the same value. 

# Return the number of clumps in the given array.



# count_clumps([1, 2, 2, 3, 4, 4]) -> 2

# count_clumps([1, 1, 2, 1, 1]) -> 2

# count_clumps([1, 1, 1, 1, 1]) -> 1



def count_clumps(nums):

  count = 0
  if len(nums) == 0:
    return count
  prev = nums[0]
  prev2 = ""
  for i in range(1,len(nums)):
    if prev == nums[i]:
      if prev2 == prev:
        pass
      else:
        count = count + 1
    prev2 = prev
    prev = nums[i]
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

    [2, [1,2,2,3,4,4]],

    [2, [1,1,2,1,1]],

    [1, [1,1,1,1,1]],

    [0, [1,2,3]],

    [4, [2,2,1,1,1,2,1,1,2,2]],

    [4, [0,2,2,1,1,1,2,1,1,2,2]],

    [5, [0,0,2,2,1,1,1,2,1,1,2,2]],

    [5, [0,0,0,2,2,1,1,1,2,1,1,2,2]],

    [0, []]]



  count = 0

  total = len(args)

  for arg in args:

    result = count_clumps(arg[1])

    is_correct = result == arg[0]

    if is_correct:

      count += 1

    print showMessage(is_correct, "count_clumps", arg, result)

  if count == total:

    print "All Correct!"

  else:

    print "passed " + str(count) + " out of " + str(total)



main()
