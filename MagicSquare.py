#  File: MagicSquare.py

#  Description: Tests an input file to validate if each matrix is a perfect square.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 11/02/10

#  Date Last Modified: 11/03/10

#import necessary libraries
import string
import sys

#isMagic function: returns true if matrix is magic. input: 2-D list. output: True/False retriction: must be square matrix
def isMagic(b):
  n = len(b) 

#checks to see that each number is not repeated
  new = []
  for i in b:
    for j in i:
      new.append(j)
  for i in new:
    if new.count(i) > 1:
      return False

#calculating the goal sum of each row/column/diagonal
  sum = 0
  for i in b:
    for j in i:
      sum += int(j)
  sum = sum / n

#calculating the sum of each row
  for elt in b:
    s = 0
    for item in elt:
      s += int(item)
    if s != sum:
        return False

#calculating the sum of each column
  for i in range (n):
    s = 0
    for j in range (n):
      s += int(b[j][i])
    if s != sum:
      return False

#calculating the sum of each diagonal
  s = 0
  for i in range (n):
    s += int(b[i][i])
  if s != sum:
    return False
  s = 0
  for i in range (n):
    s += int(b[i][n-1-i])
  if s != sum:
    return False
  return True

#main function: prints verification to output file. input: name of input and output file. output: verifications written to output file
def main():

#enetering file names
  infile = raw_input ("Enter name of input file: ")
  outfile = raw_input ("Enter name of output file: ")

#error message note
  if infile == outfile:
    print "Error: input file name and output file name same"
    sys.exit()

#opening and reading the file
  input = open (infile, "r")
  content = input.read()
  idx = content.find("\n")
  num = int(content[0])
  output = open (outfile, "w")

#begin writing the output file
  output.write(content[0:3])
  content = content[2:]

#loop to seperate the different matrices
  while num > 0:
    content = content[1:]
    dim = int(content[0])
    origdim = content[0]
    start = 0
    idx = 0
    b = []
    content = content[2:]

#loop to make each martix a list
    while dim > 0:
      idx = content.find("\n",idx+1)
      line = content[start:idx].split()
      b.append(line)
      dim = dim - 1
      start = idx + 1

#placing each matrix through function
    if isMagic(b):
      a = "valid"
    else:
      a = "invalid"

#Writing everything to the output file
    output.write(origdim + " " + a + "\n" + content[:idx+1] + "\n")
    content = content[idx+1:]
    num = num - 1
  input.close()
  output.close()

#printing final statement
  print "\n" + "The output has been written to %s" % outfile

main()