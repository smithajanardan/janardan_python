
#  File: count_triple.py 

#  Description: Returns the number of triple same-number sequences.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/28/10

#  Date Last Modified: 10/28/10



# We'll say that a "triple" in a string is a char appearing 

# three times in a row. Return the number of triples in the 

# given string. The triples may overlap.



# count_triple("abcXXXabc") -> 1
# count_triple("xxxabyyyycd") -> 3

# count_triple("a") -> 0



def count_triple(str):

  count = 0
  if len(str) <= 2:
    return count
  prev = str[0]
  prev2 = str[1]
  for i in range(2,len(str)):
    if str[i] == prev and str[i] == prev2:
      count = count + 1
    prev2 = prev
    prev = str[i]
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

    [1, "abcXXXabc"],

    [3, "xxxabyyyycd"],

    [0, 'a'],

    [0, ''],

    [1, 'XXXabc'],

    [2, 'XXXXabc'],

    [3, 'XXXXXabc'],

    [3, '222abyyycdXXX'],

    [4, 'abYYYabXXXXXab'],

    [0, 'abYYXabXXYXXab'],

    [0, 'abYYXabXXYXXaa'],

    [1, '122abhhh2']]



  count = 0

  total = len(args)

  for arg in args:

    result = count_triple(arg[1])

    is_correct = result == arg[0]

    if is_correct:

      count += 1

    print showMessage(is_correct, "count_triple", arg, result)

  if count == total:

    print "All Correct!"

  else:

    print "passed " + str(count) + " out of " + str(total)



main()