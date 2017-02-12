#  File: Goldbach.py

#  Description: This programs returns all even numbers from 4 to 100 as a sum of two prime numbers.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/5/10

#  Date Last Modified: 10/8/10

import math
#importing the math library to use the math functions

def isPrime(n):
#isPrime that was coded in class
  limit = int(math.sqrt(n)) + 1
  for i in range (2,limit):
    if (n % i == 0):
      return False
  return True

def main():
  for i in range (4,101,2):
#starting off with the original number being all evens from 4-100
    start = ""
#an empty set to start the sequence
    for j in range (2,i/2 + 1):
      secondNum = i-j
#secondNum is the difference between the original number and the first number
      if isPrime(j) and isPrime(secondNum) and secondNum != 1:
#testing to see if each number is prime
        sequence = " = " + str(j) + " + " + str(secondNum)
        start = start + sequence
#stringing all of the numbers, =/+, and other combinations together
    wholeSequence = str(i) + start
#combining the sequence with the original number
    print wholeSequence

main()