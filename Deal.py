#  File: Deal.py

#  Description: Run the Let's Make A Deal Similuation x number of times to determine if switching is better or worse.

#  Student Name: Smitha

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 11/15/10

#  Date Last Modified: 11/15/10

#import necessary libraries
import random

#main function: runs make a deal simulation input: number of simulations output: probabilites
def main():

#user input number of simuations
  num = input ("Enter number of times you want to play: ")
  switchNum = 0
  origNum = num
  print "\n", "Prize".center(9), "Guess".center(13), "View".center(10), "New Guess".center(11)

#in loop: randomly picks "prize" and "guess", calculates "view" and "newGuess"
  while num > 0:
    prize = random.randrange(1,4)
    guess = random.randrange(1,4)
    view = 1
    while view == prize or view == guess:
      view += 1
    newGuess = 1
    while newGuess == guess or newGuess == view:
      newGuess += 1
    print str(prize).center(9), str(guess).center(13), str(view).center(10), str(newGuess).center(11)

#if correct, the number of wins increase by one
    if newGuess == prize:
      switchNum += 1
    num += -1 

#print final statement about probabilty of switcing versus not
  prob =  float(switchNum)/origNum
  print "\n", "Probability of winning if you switch = %0.2f" % prob
  print "Probability of winning if you do not switch = %0.2f" % (1-prob)

main()