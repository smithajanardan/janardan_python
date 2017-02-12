
#  File: count_yz.py 

#  Description: Counts the number of Zs and Ys at the end of each word

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10



# Given a string, count the number of words ending 

# in 'y' or 'z' -- so the 'y' in "heavy" and the 'z' 

# in "fez" count, but not the 'y' in "yellow" (not 

# case sensitive). We'll say that a y or z is at the 

# end of a word if there is not an alphabetic letter 

# immediately following it. (Note: char.isalpha() tests 

# if a char is an alphabetic letter.)



# count_yz("fez day") -> 2

# count_yz("day fez") -> 2

# count_yz("day fyyyz") -> 2



def count_yz(str):

  count = 0
  str = str.lower()
  prev = str[0]
  for i in range(1, len(str)):
    if (not str[i].isalpha()) and (prev == "y" or prev == "z"):
      count = count + 1
    prev = str[i]
  if (str[len(str)-1] == "y") or (str[len(str)-1] == "z"): 
    count = count + 1
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

    [2, "fez day"],

    [2, "day fez"],

    [2, "day fyyyz"],

    [1, "day yak"],

    [1, "day:yak"],

    [2, "!!day--yaz!!"],

    [0, "yak zak"],

    [2, "DAY abc XYZ"],

    [3, "aaz yyz, my"],

    [2, "y2bz"],

    [0, "zxyx"]]



  count = 0

  total = len(args)

  for arg in args:

    result = count_yz(arg[1])

    is_correct = result == arg[0]

    if is_correct:

      count += 1

    print showMessage(is_correct, "count_yz", arg, result)

  if count == total:

    print "All Correct!"

  else:

    print "passed " + str(count) + " out of " + str(total)



main()