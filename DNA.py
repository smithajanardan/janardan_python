#  File: DNA.py

#  Description: Providing the largest common subsequence(s) of two DNA strands.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 5220

#  Date Created: 10/11/10

#  Date Last Modified: 10/11/10

import string
#Enabling the string library

def main():

  first = raw_input ("Enter first strand: ")
  second = raw_input ("Enter second strand: ")
#Inputing each sequence as a string

  first_size = len(first)
  second_size = len(second)
#Finding the length of each sequence

  z = cmp (first_size, second_size)
  if z <= 0:
    main = first
    size = first_size
    other = second
  elif z > 0:
    main = second
    size = second_size
    other = first
#Finding the shorter sequence and setting to common variables

  str = ""
  for ch in range (0, size-1):
    if str != "":
      break
#Stopping if a common sequence is already found

    ch = size - ch
#setting the string length from biggest to smallest

    for beg in range (0, size-ch+1):
      sub_str = main[beg: ch + beg]
#Finding all the substrings of length c

      if other.find(sub_str) != -1:
        str = str + "\n" + sub_str
#Determining if the substring is present in the larger sequence

  print ""
  if str == "":
    print "No Common Sequence Found."
#Printing an error is no sequences is found

  else:
    print "Common Subsequence(s):"
    print str.replace ("\n", "", 1)
#Printing the sequence with out the first space

main()
