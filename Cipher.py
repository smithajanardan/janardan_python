#  File: Cipher.py

#  Description: Takes a file and either decrpyts or encrypts the text file onto a new text file.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/15/10

#  Date Last Modified: 10/19/10

#importing the necessary librarys
import sys
import string

#encrpyt function: encrpyts a text file. input: input file, shift parameter, and output file. output: encrypted output file.
def encrypt(input, num, output): 
  incode = open (input, "r")
  content = incode.read()
  incode.close()
  str = ""
  for line in content:

#for all numbers and letters
    if line.isalnum():

#arbitrary n assigned to numerical value of each character
      n = ord(line)
      new = n + num

#shifiting character num characters up (with a wrap)
      if n in range(65,91):
        while new not in range(65,91):
          new = new - 26
      elif n in range(97,123):
        while new not in range(97,123):
          new = new - 26
      elif n in range (48,58):
        while new not in range(48,58):
          new = new - 10
      line = chr(new)
    str = str + line 

#writing the new code into the output file
  outcode = open (output, "w")
  outcode.write (str)
  outcode.close()

#decrpyt function: decrpyts a text file. input: input file, shift parameter, and output file. output: decrypted output file.
def decrpyt(input, num, output):
  incode = open (input, "r")
  content = incode.read()
  incode.close()
  str = ""
  for line in content:

#for all numbers and letters
    if line.isalnum():

#arbitrary n assigned to numerical value of each character
      n = ord(line)
      new = n - num

#shifiting it num characters down (with a wrap)
      if n in range(65,91):
        while new not in range(65,91):
          new = new + 26
      elif n in range(97,123):
        while new not in range(97,123):
          new = new + 26
      elif n in range (48,58):
        while new not in range(48,58):
          new = new + 10
      line = chr(new)
    str = str + line

#writing the new code into the output file
  outcode = open (output, "w")
  outcode.write (str)
  outcode.close()

#main function: interface options. input: decode/encode option, input file, shift parameter, output file.output: computed output file
def main():

#if option is not entered properly, program is quitted
  code = raw_input ("Do you want to encrypt or decrpyt? (E / D): ")
  if code != "E" and code != "D":
    print "Invalid Input"
    sys.exit()

#normal input methods
  infile = raw_input ("Enter name of input file: ")
  shift = input ("Enter shift parameter: ")
  if shift%1.0 != 0  or shift <= 0:
    print "Invalid Input"
    sys.exit()
  outfile = raw_input ("Enter name of output file: ")
  if code == "E":
    encrypt(infile, shift, outfile)
  if code == "D":
    decrpyt(infile, shift, outfile)

#printing confirmation of coding
  print "\n", "Output written to %s" % outfile

main()