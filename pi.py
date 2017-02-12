import random

def main():
  n = input ("Enter a number: ")
  a = n
  count = 0
  while a > 0:
     x = random.random()
     y = random.random()
     if ((x**2) + (y**2)) <= 1:
       count = count + 1
     a = a-1
  print ((count/float(n))*4)
main()