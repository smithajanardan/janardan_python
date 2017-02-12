#  File: CalcSqrt.py

#  Description: Determining the square root of a poistive integer.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 09-29-10

#  Date Last Modified: 09-29-10

def main():
  n = input ("Enter a positive number: ")
  while n < 0:
    print "Error: input not in range"
    n = input ("Enter a positive number: ")
  oldGuess = 0
  newGuess = n/2.0
  while abs(oldGuess - newGuess) > .000001:
    oldGuess = newGuess
    newGuess = ((n / oldGuess) + oldGuess) / 2.0
  diff = newGuess - ( n ** .5 )
  print "Square root is: ", newGuess
  print "Difference is: ", diff

main()