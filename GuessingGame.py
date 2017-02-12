#  File: GuessingGame.py

#  Description: Guesses a number between 1 and 100 based on user responces.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 11/10/10

#  Date Last Modified: 11/10/10

#importing necessary libraries
import string
import sys

#main function: guess number. input: readiness, right/wrong. output: guess of number
def main():

#printing beginning lines
  print "\nGuessing Game\n\nThink of a number between 1 and 100 inclusive.\nAnd I will guess what it is in 7 tries or less.\n" 

#input readiness with only "y" acceptable
  ready = raw_input ("Are you ready? (y/n): ")
  while ready != "y":
    ready = raw_input ("Are you ready? (y/n): ")

#base case
  num = 7
  high = 100
  low = 1

#while loop to guess numbers
  while num > 0:
    mid = (high + low)/2

#asks user if guess too high, too low, or just right
    print "\nGuess %d :  The number you thought was %d" % (8-num, mid)
    guess = input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
    while (guess != 1) and (guess != -1) and (guess != 0):
      guess = input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")

#changes base case if guess was incorrect
    if guess == 1:
      high = mid
      num = num - 1
    elif guess == -1:
      low = mid
      num = num - 1

#exits program if guess is correct
    elif guess == 0:
      print "\nThank you for playing the Guessing Game."
      sys.exit()

#informs user that number is not in range
  print "\nThe number you thought of is not between 1 and 100."

main()

