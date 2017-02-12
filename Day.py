#  File: Day.py

#  Description: Defining the name of the day, given the day, month and year.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 09-18-10

#  Date Last Modified: 09-18-10

def main():
  import string
  import math, random
  b = input ("Enter day: ")
  while b not in range (1,32):
    b = input ("Enter day: ")
  a = input ("Enter month: ")
  while a not in range (1,13):
    a = input ("Enter month: ")
  c = input ("Enter year: ")
  while c not in range (1900,2101):
    c = input ("Enter year: ")
  if a in [1, 2]:
    a = a + 10
    c = c - 1
  else:
    a = a - 2
  h = str(c)
  g = h[2:]
  i = h[:2]
  c = int(g)
  d = int(i)
  w = (13 * a - 1) / 5
  x = c / 4
  y = d / 4
  z = w + x + y + b + c - 2 * d
  r = z % 7
  r = (r + 7) % 7
  if r == 0:
    n = "Sunday."
  elif r == 1:
    n = "Monday."
  elif r == 2:
    n = "Tuesday."
  elif r == 3:
    n = "Wednesday."
  elif r == 4:
    n = "Thursday."
  elif r == 5:
    n = "Friday."
  else:
    n = "Saturday."
  print ""
  print "This day is", n

main()