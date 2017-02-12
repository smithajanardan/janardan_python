#  File: MagicSquare.py

#  Description: Creates a magic square of a given size.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 02/01/11

#  Date Last Modified: 02/03/11

# Populate a 2-D list with numbers from 1 to n2
def makeSquare ( n ):
  square = []
  for i in range (n):
    a = []
    for j in range (n):
      a.append (0)
    square.append(a)
  row = n-1
  column = n/2
  square [row][column] = 1
  for i in range (2,(n**2)+1):
    row2 = row
    row += 1
    if row >= n:
      row += -n
    column2 = column
    column += 1
    if column >= n:
      column += -n
    if square[row][column] != 0:
      square[row2-1][column2] = i
      row = row2-1
      column = column2
    else:
      square[row][column] = i
  return square

# Print the magic square in a neat format where the numbers
# are right justified
def printSquare ( magicSquare ):
  print
  for elt in magicSquare:
    for item in elt:
      print str(item).rjust(4),
    print


# Check that the 2-D list generated is indeed a magic square
def checkSquare ( magicSquare, n ):

#calculating the goal sum of each row/column/diagonal
  print
  sum = n * (n**2 + 1) / 2

#calculating the sum of each row
  for elt in magicSquare:
    s = 0
    for item in elt:
      s += item
    if s != sum:
        print "error"
  print "Sum of row = ", s

#calculating the sum of each column
  for i in range (n):
    s = 0
    for j in range (n):
      s += magicSquare[j][i]
    if s != sum:
      print "error"
  print "Sum of column = ", s

#calculating the sum of each diagonal
  s = 0
  for i in range (n):
    s += magicSquare[i][i]
  if s != sum:
    print "error"
  print "Sum diagonal (UL to LR) = ", s
  s = 0
  for i in range (n):
    s += magicSquare[i][n-1-i]
  if s != sum:
    print "error"
  print "Sum diagonal (UR to LL) = ", s


def main():
  # Prompt the user to enter an odd number 3 or greater
  n = input("Please enter an odd integer that is 3 or greater: ")

  # Check the user input
  while n % 2 != 1 or n < 3:
    n = input("Please enter an ODD INTEGER that is 3 or GREATER: ")

  # Create the magic square
  square = makeSquare (n)

  # Print the magic square
  printSquare (square)

  # Verify that it is a magic square
  checkSquare (square, n)

main()