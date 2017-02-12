#  File: ISBN.py

#  Description: Checks if ISBN numbers in input file are valid and prints to output file.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/26/10

#  Date Last Modified: 10/27/10

import string

#verifing function: returns true if string is valid. input = one string. output = True/False. restrictions = one line at a time only
def check(str):

#checking if the string has other characters than numbers, Xs, or  dashes
  for i in str:
    if (not i.isdigit()) and (i != "x") and (i != "X") and (i != "-"):
      return False

#getting rid of the dashes
  str = str.replace("-","")

#verifying the only X present is the last value
  for j in range(len(str)-1):
    if (not str[j].isdigit()):
      return False

#verifying the string is 10 digits
  if len(str) != 10:
    return False

#turing the string into a list
  str = list(str)
  sum = 0
  s1 = []

#changing the x (if present) into the number 10
  for k in str:
    if k == "x" or k == "X":
      k = 10

#making all the strings intergers for addition into the sum
    k = int(k)
    sum = sum + k

#creating the s1 list from the sums
    s1.append(sum)
  s2 = []
  sum = 0

#finding the summation of s1
  for l in s1:
    sum = sum + l
    s2.append(sum)

#final check to see if divisible by 11
  if sum % 11 == 0:
    return True
  else:
    return False

def main():

#opening the input file and reading it onto a string
  incode = open ("isbn.txt", "r")
  content = incode.read()
  incode.close()

#writing all the verifications to the output file
  outcode = open ("isbnOut.txt", "w")
  index = content.find("\n")

#seperating code by different lines
  while index >= 0:
    code = content[:index]

#if the code is a valid ISBN, attaching the string valid/invalid
    if check(code):
      b = "valid"
    else:
      b = "invalid"
    s = code + " " + b + "\n"

#writing everything in output file and closing output file
    outcode.write (s)
    content = content[index+2:]
    index = content.find("\n")

#repeating previous steps for the last line
  if check(content):
    b = "valid"
  else:
    b = "invalid"
  s = content + " " + b + "\n"
  outcode.write (s)
  outcode.close()

main()