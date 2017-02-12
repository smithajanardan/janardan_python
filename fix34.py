
#  File: fix34.py 

#  Description: Moves all the fours after a three.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10



# Return an array that contains exactly the same numbers as the 

# given array, but rearranged so that every 3 is immediately 

# followed by a 4. Do not move the 3's, but every other number 

# may move. The array contains the same number of 3's and 4's, 

# every 3 has a number after it that is not a 3 or 4, and a 3 

# appears in the array before any 4.



# fix34([1, 3, 1, 4]) -> [1, 3, 4, 1]

# fix34([1, 3, 1, 4, 3, 1, 4]) -> [1, 3, 4, 1, 3, 4, 1]

# fix34([3, 2, 2, 4]) -> [3, 4, 2, 2]



def fix34(nums):
  idx_4 = 0
  for i in range(len(nums)):
    if nums[i] == 3:
      idx_4 = nums.index(4,idx_4)
      nums[i + 1], nums[idx_4] = nums[idx_4], nums[i+1]
  return nums

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
    [[1,3,4,1], [1,3,1,4]],
    [[3,4,2,2], [3,2,2,4]],
    [[3,4,3,4,2,2], [3,2,3,2,4,4]],
    [[2,3,4,3,4,2,2], [2,3,2,3,2,4,4]],
    [[3,4,1], [3,1,4]],
    [[3,4,1], [3,1,4]],
    [[1,1,1], [1,1,1]],
    [[1], [1]],
    [[], []],
    [[7,3,4,7,7], [7,3,7,7,4]],
    [[3,4,1,3,4,1], [3,1,4,3,1,4]],
    [[3,4,1,3,4,1], [3,1,1,3,4,4]]]

  count = 0
  total = len(args)
  for arg in args:
    result = fix34(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "fix34", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()