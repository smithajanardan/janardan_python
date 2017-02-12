#  File: Nim.py

#  Description: In the gmae of Nim, find the winning move given different heap sizes.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 1/23/11

#  Date Last Modified: 1/27/11

def main():

# open file with nim games
  infile = open ("nim.txt", "r")

#find the number of games in file
  num = int(infile.readline())

#take all heap info into program
  content = infile.read()

#close input file
  infile.close()

#split content into individual games
  content = content.split("\n")

#Split games into individual heaps
  for i in range(num):
    content[i] = content[i].split()
    nimSum = 0

#find the nim sum of all heaps
    for j in range(len(content[i])):
      content[i][j] = int(content[i][j])
      nimSum = nimSum ^ content[i][j]

#determine if game is possible to win or not
    if nimSum == 0:
      print "Lose Game"

#find which heap to remove counters from
    else:
      for k in range(len(content[i])):
        nimSum2 = nimSum ^ content[i][k]
        if nimSum2 < content[i][k]:
          print "Remove %d counters from Heap %d" % (content[i][k]-nimSum2, k + 1)
          break

main()