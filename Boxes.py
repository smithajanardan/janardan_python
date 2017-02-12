#  File: Boxes.py

#  Description: Similuates placing boxes into other boxes. Finds greates number of boxes that fits.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 03/7/11

#  Date Last Modified: 03/10/11

#create the global varaibles for the biggest nested set
MAX = 0

NEST = []

#define class Box for each box in boxes.txt
class Boxes (object):

#non-default constuctor that creates the dimensions of the box in a list form
  def __init__(self, xyz):
    self.x = int(xyz[0])
    self.y = int(xyz[1])
    self.z = int(xyz[2])
#use slection sort method to sort each box dimensions
    self.size = self.selectionSort([self.x, self.y, self.z])

#sort the list using the compare function
  def selectionSort (self, a):
    for i in range (len(a) - 1):
      min = a[i]
      minIdx = i
      for j in range (i + 1, len(a)):
        if (a[j] < min):
          min = a[j]
	  minIdx = j
      a[minIdx] = a[i]
      a[i] = min
    return a

#override the compare function to suit the box class
  def __cmp__(self, other):
    if self.size[0] < other.size[0]:
      return -1
    elif self.size[0] > other.size[0]:
      return 1
    else:
      return 0

#function Doesfit: if one box fit into the other box returs True
  def Doesfit (self, other):
    for i in range(3):
      if self.size[i] >= other.size[i]:
        return False
    return True

#prints the box in a string friendly format
  def __str__(self):
    return "(" + str(self.size[0]) + ", " + str(self.size[1]) + ", " + str(self.size[2]) + ")"

#finds all combinations of boxes in boxes
def combine (a, b, idxA):

#allow the global variables to change
  global MAX
  global NEST

#if a bigger nested set is found, replace the old biggest
  if (idxA == len(a)):
    if (len(b) > 0):
      if len(b) > MAX:
        MAX = len(b)
        NEST = b
      return
  else:
    c = b[:]

#only adds the box to the list if the box fits into the other box
    if len(b) == 0 or b[-1].Doesfit(a[idxA]):
      b.append (a[idxA])
      idxA = idxA + 1
      combine (a, b, idxA)
      combine (a, c, idxA)

#if it does not fit, keeps going
    else:
      idxA = idxA + 1
      combine (a, c, idxA)

def main():

#opens the file with boxes in read format
  infile = open("boxes.txt", "r")

#find the the number of boxes
  num = int(infile.readline().rstrip("\n"))
  allBoxes = []

#makes each box into the object Box
  while num > 0:
    box = infile.readline().rstrip("\n")
    box = box.split()
    box = Boxes (box)
    allBoxes.append(box)
    num -= 1

#closes the input file
  infile.close()

#sorts the boxes by the smallest dimension
  allBoxes = sorted(allBoxes)

#sends the list of boxes to the combination function
  combine(allBoxes, [], 0)

#prints out the largest nesting set of boxes
  print "\nLargest Subset of Nesting Boxes" 
  for elt in NEST:
    print elt

main()