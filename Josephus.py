#  File: Josephus.py

#  Description: Given the Josephus problem, print the order in which the men are killed.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 313E

#  Unique Number: 53330 

#  Date Created: 03/20/11

#  Date Last Modified: 03/24/11

#Link class created in class
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

#Linked List that is a circle instead of a 1D list
class CircularList(object):

  # Constructor
  def __init__ ( self ): 
    self.last = None

  # Insert an element in the list
  def insert ( self, item ):
    newLink = Link (item)
  
  #null case puts the new link in an empty list
    if (self.last == None):
      newLink.next = newLink
      self.last = newLink

  #otherwise, adds the new link to the end of the list
    else:
      newLink.next = self.last.next
      self.last.next = newLink

  # Find the link with the given key
  def find ( self, key ):

    #create an index to trasverse the list
    current = self.last

    #for null case, return None
    if (current == None):
      return None

    #transverse the list looking for the desired key
    while (current.data != key):
      if (current.next == self.last):
        return None
      else:
        current = current.next
    return current

  # Delete a link with a given key
  def delete ( self, key ):

    #create indices to trasverse list
    current = self.last.next
    previous = self.last

    #for null case, return None
    if (current == None):
      return None

    #transverse list looking for desired key
    while (current.data != key):
      if (current.next == self.last.next):
        return None
      else:
        previous = current
	current = current.next

    #delete the link by reattaching links
    previous.next = current.next
    if (current == self.last):
      self.last = self.last.next

    return current

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n ):

    #create index form starting person to trasverse list
    current = self.find(start)

    #find the nth person from the starting person
    while n > 0:
      current = current.next
      n -= 1

    #delete that person from the list
    print current.data
    self.delete(current.data)
    return current.next

  # Return a string representation of a Circular List
  def __str__ ( self ):

    #create indexto trasverse list
    current = self.last.next

    #print each link in string format
    while (current.next != self.last.next):
      print current.data,
      current = current.next
    return " " + str(current.data)

def main():

  #open file with army data
  input = open ("josephus.txt", "r")

  #read the file to find the starting person, number of people, and shift number
  num = int(input.readline().rstrip("\n"))
  first = int(input.readline().rstrip("\n"))
  n = int(input.readline().rstrip("\n"))

  #close input file
  input.close()

  #create a Circle linked list
  links = CircularList()

  #make links out of each person's number
  for i in range(num):
    links.insert(num-i)

  #kill people off, based on shift and starting person.
  while num > 0:
    first = links.deleteAfter(first, n-1).data
    num -= 1
  
main()
