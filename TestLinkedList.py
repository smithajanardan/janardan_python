#  File: TestLinkedList.py

#  Description: Functions for a linked list, necessary for test

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 313E

#  Unique Number: 53330

#  Date Created: 03/28/11

#  Date Last Modified: 04/02/11

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # get number of links 
  def getNumLinks (self):
    current = self.first
    sum = 1
    if (current == None):
      return 0
    while (current.next != None):
      sum += 1
      current = current.next
    return sum
  
  # Add data at the beginning of the list
  def addFirst (self, data):
    newLink = Link (data)
    newLink.next = self.first
    self.first = newLink

  # Add data at the end of a list
  def addLast (self, data): 
    newLink = Link (data)
    current = self.first
    if (current == None):
      self.first = newLink
      return
    while (current.next != None):
      current = current.next
    current.next = newLink

  # Add data in an ordered list
  def addInOrder (self, data): 
    if not self.isSorted():
      return "List not Sorted"
    newLink = Link (data)
    current = self.first
    previous = self.first
    if (current == None):
      self.first = newLink
      return
    while (current != None):
      if (current.data <= data):
        previous = current
        current = current.next
      else:
        break
    if (self.first.data >= data):
      newLink.next = self.first
      self.first = newLink
    elif (current == None):
      previous.next = newLink
    else:
      previous.next = newLink
      newLink.next = current

  # Search in an unordered list, return None if not found
  def findUnordered (self, data): 
    current = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next
    return current

  # Search in an ordered list, return None if not found
  def findOrdered (self, data): 
    if not self.isSorted():
      return "List not Sorted"
    current = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      elif (current.data > data):
        return None
      else:
        current = current.next
    return current

  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
    current = self.first
    previous = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
	current = current.next
    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next
    return current

  # Print contents of a list, 10 items to a line, 2 spaces between items
  def printList (self):
    current = self.first
    while (current != None):
      print current.data,
      current = current.next
    print
    return ""

  # Copy the contents of a list and return new list
  def copyList (self):
    new = LinkedList ()
    current = self.first
    while (current != None):
      new.addLast(current.data)
      current = current.next
    return new

  # Reverse the contents of a list and return new list
  def reverseList (self): 
    new = LinkedList ()
    current = self.first
    while (current != None):
      new.addFirst(current.data)
      current = current.next
    return new

  # Sort the contents of a list in ascending order and return new list
  def sortList (self): 
    new = LinkedList ()
    current = self.first
    while (current != None):
      new.addInOrder(current.data)
      current = current.next
    return new

  # Test if a list is sorted in ascending order
  def isSorted (self):
    previous = self.first
    if (previous == None):
      return True
    current = self.first.next
    while (current != None):
      if current.data < previous.data:
        return False
      previous = current
      current = current.next
    return True

  # Test if a list is empty
  def isEmpty (self): 
    return self.first == None

  # Merge two sorted lists and return new list
  def mergeList (self, b): 
    new = LinkedList ()
    if (not self.isSorted()) or (not b.isSorted()):
      return "Lists not sorted"
    current = self.first
    current2 = b.first
    while (current != None) and (current2 != None):
      if current.data < current2.data: 
        new.addLast(current.data)
        current = current.next
      else:
        new.addLast(current2.data)
        current2 = current2.next
    while (current != None):
      new.addLast(current.data)
      current = current.next
    while (current2 != None):
      new.addLast(current2.data)
      current2 = current2.next
    return new

  # Test if two lists are equal, item by item
  def isEqual (self, b):
    current = self.first
    current2 = b.first
    while (current != None) and (current2 != None):
      if (current.data != current2.data):
        return False
      current = current.next
      current2 = current2.next
    if (current2 != None) or (current != None):
      return False
    return True

  # Remove duplicates and return a new list without the duplicates
  def removeDuplicates (self):
    list = []
    new = LinkedList ()
    current = self.first
    while (current != None):
      list.append(current.data)
      current = current.next
    list = set (list)
    for elt in list:
      new.addLast(elt)
    return new

  def __str__(self):
    current = self.first
    while (current != None):
      print current.data,
      current = current.next
    print
    return ""

def main():
  # Test methods addFirst() and printList() by adding more than
  # 10 items to a list and printing it.
  print "Test methods addFirst() and printList()"
  test1 = LinkedList ()
  num = 15
  while num > 0:
    test1.addFirst(num)
    num -= 1
  test1.printList()

  # Test method addLast()
  print "Test method addLast()"
  test2 = LinkedList ()
  while num <= 15:
    test2.addLast(num)
    num += 1
  test2.addFirst(764)
  test2.printList()
  print

  # Test method addInOrder()
  print "Test method addInOrder()"
  test1.addInOrder(0)
  test1.addInOrder("lol")
  test1.addInOrder(15)
  test1.addInOrder(6)
  test1.addInOrder("aaa")
  test2.addInOrder("bbb")
  test1.printList()
  print
  
  # Test method getNumLinks()
  print "Test method getNumLinks()"
  test3 = LinkedList ()
  print test1.getNumLinks()
  print test2.getNumLinks()
  print test3.getNumLinks()
  print

  # Test method findUnordered() 
  # Consider two cases - item is there, item is not there 
  print "Test method findUnordered()"
  print test2.findUnordered(764)
  print test1.findUnordered(7)
  print test3.findUnordered(7534)

  # Test method findOrdered() 
  # Consider two cases - item is there, item is not there
  print "Test method findOrdered() "
  print test2.findOrdered(764)
  print test1.findOrdered(7)
  print test1.findOrdered(342)
  print test3.findOrdered(7534)
  print

  # Test method delete()
  # Consider two cases - item is there, item is not there
  print "Test method delete()"
  print test3.delete(7534)
  print test1.delete(5)
  print test1.delete(73)
  print

  # Test method copyList()
  print "Test method copyList()"
  test4 = test1.copyList()
  test4.printList()

  # Test method reverseList()
  print "Test method reverseList()"
  print test1.reverseList()

  # Test method sortList()
  print "Test method sortList()"
  print test2.sortList()
  print

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
  print "Test method isSorted()"
  print test2.isSorted()
  print test1.isSorted()
  print test3.isSorted()
  print

  # Test method isEmpty()
  print "Test method isEmpty()"
  print test2.isEmpty()
  print test1.isEmpty()
  print test3.isEmpty()
  print

  # Test method mergeList()
  print "Test method mergeList()"
  print test2.mergeList(test1)
  print test1.mergeList(test1)
  print test1.mergeList(test3)
  print

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  print "Test method isEqual()"
  print test2.isEqual(test1)
  print test4.isEqual(test1)
  print test3.isEqual(test1)
  print

  # Test removeDuplicates()
  print "Test removeDuplicates()"
  test1.removeDuplicates().printList()

main()