class Stack (object):
  def __init__ (self):
    self.stack = []

  def push (self, item):
    self.stack.append ( item )

  def pop (self):
    return self.stack.pop()

  def peek (self):
    return self.stack[len(self.stack) - 1]

  def isEmpty (self):
    return (len(self.stack) == 0)

  def size (self):
    return (len(self.stack))

  def __str__ (self):
    for item in self.stack:
      print str(item)
    return ""

def xmlchecker():
  xmlstack = Stack()
  input = open ("Exam2.txt", "r")
  xmltext = ""
  for line in input:
    xmltext += line.rstrip("\n")
  input.close()
  for i in range (len(xmltext)):
    if xmltext[i:i+2] == "</":
      end = xmltext.index(">", i)
      tag = xmltext[i+2:end]
      tag2 = xmlstack.pop()
      if tag2 != tag:
        return False
    elif xmltext[i] == "<":
      end = xmltext.index(">", i)
      tag = xmltext[i+1:end]
      xmlstack.push (tag)
  return True

def polishmath(string):
  notation = Stack()
  for chr in string:
    if chr.isspace():
      continue
    elif chr.isdigit():
      notation.push(chr)
    else:
      first = str(notation.pop())
      second = str(notation.pop())
      math = eval(first+chr+second)
      notation.push(math)
  return notation.pop()

def polishstr(string):
  notation = Stack()
  str = ""
  for chr in string:
    if chr.isspace():
      continue
    if chr.isdigit():
      notation.push(chr)
    else:
      first = notation.pop()
      second = notation.pop()
      str = "(" + first + chr + second + ")"
      notation.push(str)
  return notation.pop()

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    newLink = Link (data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)
    current = self.first
    if (current == None):
      self.first = newLink
      return
    while (current.next != None):
      current = current.next
    current.next = newLink

  def findLink (self, data):
    current = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next
    return current

  def deleteLink (self, data):
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

  def getNumLinks (self):
    current = self.first
    sum = 1
    if (current == None):
      return 0
    while (current.next != None):
      sum += 1
      current = current.next
    return sum

  def insertInorder(self, data):
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

  def findInorder(self, data):
    current = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next
    return current

  def deleteInorder(self, data):
    current = self.first
    previous = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      elif (current.data > data):
        return None
      else:
        previous = current
	current = current.next
    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next
    return current

  def copy(self):
    new = LinkedList ()
    current = self.first
    while (current != None):
      new.insertLast(current.data)
      current = current.next
    return new

  def sort(self):
    new = LinkedList ()
    current = self.first
    while (current != None):
      new.insertInorder(current.data)
      current = current.next
    return new

  def reverse(self):
    new = LinkedList ()
    current = self.first
    while (current != None):
      new.insertFirst(current.data)
      current = current.next
    return new

  def isSorted(self):
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

  def isEqual(self, other):
    current = self.first
    current2 = other.first
    while (current != None) and (current2 != None):
      if (current.data != current2.data):
        return False
      current = current.next
      current2 = current2.next
    if (current2 != None) or (current != None):
      return False
    return True

  def removeDuplicates(self):
    list = []
    new = LinkedList ()
    current = self.first
    while (current != None):
      list.append(current.data)
      current = current.next
    list = set (list)
    for elt in list:
      new.insertLast(elt)
    return new

  def replaceLink(self, key, data):
    replace = self.findLink (key)
    while (replace != None):
      replace.data = data
      replace = self.findLink (key)
    return self

  def merge(self, other):
    new = LinkedList ()
    if (not self.isSorted()) or (not other.isSorted()):
      return "Lists not sorted"
    current = self.first
    current2 = other.first
    while (current != None) and (current2 != None):
      if current.data < current2.data: 
        new.insertLast(current.data)
        current = current.next
      else:
        new.insertLast(current2.data)
        current2 = current2.next
    while (current != None):
      new.insertLast(current.data)
      current = current.next
    while (current2 != None):
      new.insertLast(current2.data)
      current2 = current2.next
    return new

  def __str__(self):
    current = self.first
    while current != None:
      print current.data,
      current = current.next
    return ""

class DoubleLink (object):

  def __init__(self, data, next = None, prev = None):
    self.data = data
    self.next = next
    self.prev = prev

class DoubleLinkedList (object):

  def __init__(self):
    self.first = None
    self.last = None

  def insertFirst(self, data):
    newLink = DoubleLink (data)
    current = self.first
    if (current == None):
      self.first = newLink
      self.last = newLink
      return
    self.first.prev = newLink
    newLink.next = self.first
    self.first = newLink

  def insertLast(self, data):
    newLink = DoubleLink (data)
    current = self.last
    if (current == None):
      self.first = newLink
      self.last = newLink
      return
    self.last.next = newLink
    newLink.prev = self.last
    self.last = newLink

  def findLink(self, data):
    current = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next
    return current

  def deleteLink(self, data):
    current = self.first
    previous = self.first
    next = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
	current = current.next
	next = current.next
    if (current == self.first):
      self.first = self.first.next
    elif (current == self.last):
      previous.next = current.next
    else:
      previous.next = next
      next.prev = previous
    return current

  def __str__(self):
    current = self.first
    while current != None:
      print current.data,
      current = current.next
    return ""
    return ""
    
def main():
  print xmlchecker()
  pol = "3 2 1 + *"
  print polishmath(pol)
  print polishstr(pol)
  lol = LinkedList ()
  n = 10
  while n > 0:
    lol.insertFirst(n)
    n -= 1
  lol.insertLast(1)
  while n <= 10:
    lol.insertLast(n)
    n += 1
  print lol
  b = lol.sort()
  b.insertLast(56)
  print b
  print lol.reverse()
  c = lol.sort()
  print c
  print c.isEqual(b)
  print b.isSorted()
  print lol.isSorted()
  print lol.removeDuplicates()
  print lol.replaceLink(5, 7)
  print b.merge(c)
  haha = DoubleLinkedList()
  while n > 0:
    haha.insertFirst(n)
    n -= 1
  while n <= 10:
    haha.insertLast(n)
    n += 1
  print haha
  print haha.findLink(5).data
  print haha.deleteLink(7).data
  print haha

main()