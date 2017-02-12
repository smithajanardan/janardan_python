#  File: EasterSunday.py

#  Description: What day of each year is Easter SUnday?

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 09-08-10

#  Date Last Modified: 09-08-10

############################################################################

def main():
  y=input ("Enter Value: ")
  a = y % 19
  b = y / 100
  c = y % 100
  d = b / 4
  e = b % 4
  f = 8 * b + 13
  g = f / 25
  h = (19 * a + b - d - g + 15) % 30
  j = c / 4
  k = c % 4
  m = (a + 11 * h) / 319
  r = (2 * e + 2 * j - k - h + m + 32) % 7
  n = (h - m + r + 90) / 25
  p = (h - m + r + n + 19) % 32
  if (n == 4):
    z = "April"
  else:
    z = "March"
  if (y <= 2010):
    t = "was"
  else:
    t = "will be"
  print "In",
  print y,
  print "Easter Sunday",
  print t,
  print "on",
  print p,
  print z

main()