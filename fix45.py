#  File: fix45.py 

#  Description: Moves all fives after a three.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10

# (This is a slightly harder version of the fix34 problem.) Return 
# an array that contains exactly the same numbers as the given array, 
# but rearranged so that every 4 is immediately followed by a 5. Do 
# not move the 4's, but every other number may move. The array contains 
# the same number of 4's and 5's, and every 4 has a number after it 
# that is not a 4. In this version, 5's may appear anywhere in the 
# original array.

# fix45([5, 4, 9, 4, 9, 5]) -> [9, 4, 5, 4, 5, 9]
# fix45([1, 4, 1, 5]) -> [1, 4, 5, 1]
# fix45([1, 4, 1, 5, 5, 4, 1]) -> [1, 4, 5, 1, 1, 4, 5]

def fix45(nums):
  idx_5 = 0
  for i in range(len(nums)):
    if nums[i] == 4:
      idx_5 = nums.index(5,idx_5)
      while nums[idx_5-1] == 4:
        idx_5 = nums.index(5,idx_5+1)
      nums[i + 1], nums[idx_5] = nums[idx_5], nums[i+1]
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
    [[9,4,5,4,5,9], [5,4,9,4,9,5]],
    [[1,4,5,1,], [1,4,1,5]],
    [[1,4,5,1,1,4,5], [1,4,1,5,5,4,1]],
    [[4,5,4,5,9,9,4,5,9], [4,9,4,9,5,5,4,9,5]],
    [[1,1,4,5,4,5], [5,5,4,1,4,1]],
    [[4,5,2,2], [4,2,2,5]],
    [[4,5,4,5,2,2], [4,2,4,2,5,5]],
    [[4,5,4,5,2], [4,2,4,5,5]],
    [[1,1,1], [1,1,1]],
    [[4,5], [4,5]],
    [[1,4,5], [5,4,1]],
    [[], []],
    [[1,4,5,4,5], [5,4,5,4,1]],
    [[4,5,4,5,1], [4,5,4,1,5]],
    [[3,4,5], [3,4,5]],
    [[4,5,1], [4,1,5]],
    [[1,4,5], [5,4,1]],
    [[2,4,5,2], [2,4,2,5]]]

  count = 0
  total = len(args)
  for arg in args:
    result = fix45(arg[1])
    is_correct = result == arg[0]
    if is_correct:
      count += 1
    print showMessage(is_correct, "fix45", arg, result)
  if count == total:
    print "All Correct!"
  else:
    print "passed " + str(count) + " out of " + str(total)

main()