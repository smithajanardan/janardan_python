#  File: TestBinaryTree.py

#  Description: Functions for a binary search tree : print specific level, find height of tree, and isSimilar

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 313E

#  Unique Number: 53330

#  Date Created: 03/28/11

#  Date Last Modified: 04/02/11

#Use given node class
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

#use given tree class
class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
	if (val < current.data):
          current = current.lChild
	else:
	  current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder (aNode.lChild)
      print aNode.data
      self.inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print aNode.data
      self.preOrder (aNode.lChild)
      self.preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lChild)
      self.postOrder (aNode.rChild)
      print aNode.data

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while (deleteNode.data != key):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
	isLeft = True
      else:
        deleteNode = deleteNode.rChild
	isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild == None):
        successorParent = successor
	successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
	successor.rChild = deleteNode.rChild

    return True

  def exactCopy (self):
    newTree = Tree ()
    list = []
    levels = []
    levels.append(self.root)
    list.append(levels)
    boolean = True
    while (boolean == True):
      levels = []
      for elt in list[-1]:
        if (elt == None):
          continue
        else:
          levels.append(elt.lChild)
          levels.append(elt.rChild)
      if (levels == []):
        boolean = False
        break
      else:
        list.append(levels)
    n = self.getHeight(self.root)
    for i in range(n):
      for item in list[i]:
        if item == None:
          pass
        else:
          newTree.insert(item.data)
    return newTree

  def mirrorImage (self):
    newTree = Tree ()
    list = []
    levels = []
    levels.append(self.root)
    list.append(levels)
    boolean = True
    while (boolean == True):
      levels = []
      for elt in list[-1]:
        if (elt == None):
          continue
        else:
          levels.append(elt.lChild)
          levels.append(elt.rChild)
      if (levels == []):
        boolean = False
        break
      else:
        list.append(levels)
    n = self.getHeight(self.root)
    for i in range(n):
      for item in list[i]:
        if item == None:
          pass
        else:
          newTree.insertMirror(item.data)
    return newTree

  def insertMirror (self, val):
    newNode = Node (val)
    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
	if (val < current.data):
          current = current.rChild
	else:
	  current = current.lChild
      if (val < parent.data):
        parent.rChild = newNode
      else:
        parent.lChild = newNode


  # Returns true if two binary trees are similar
  def isSimilar (self, pNode):

#using the same method as getHeight, create a list of the levels
    list = []
    levels = []
    levels.append(self.root)
    list.append(levels)
    boolean = True
    while (boolean == True):
      levels = []
      for elt in list[-1]:
        if (elt == None):
          continue
        else:
          levels.append(elt.lChild)
          levels.append(elt.rChild)
      if (levels == []):
        boolean = False
        break
      else:
        list.append(levels)

#get list of levels for second tree
    list2 = []
    levels = []
    levels.append(pNode.root)
    list2.append(levels)
    bool = True
    while (bool == True):
      levels = []
      for elt in list2[-1]:
        if (elt == None):
          continue
        else:
          levels.append(elt.lChild)
          levels.append(elt.rChild)
      if (levels == []):
        bool = False
        break
      else:
        list2.append(levels)

#compare the two lists
    for i in range(len(list)):
      for j in range(len(list[i])):

#if list is none, then ok
        if (list[i][j] == None) and (list2[i][j] == None):
          continue

#if the data does not match, return false
        elif list[i][j].data != list2[i][j].data:
          return False
    return True

  # Prints out all nodes at the given level
  def printLevel (self, level):

#if the list is empty return nothing
    if (self.root == None):
      return None

#create two empty lists to start 2D list
    list = []
    levels = []

#start 2D list by adding the root to the inner list which is added to main list
    levels.append(self.root)
    list.append(levels)

#find the length of the main list (aka the level number)
    length = len(list)

#untill the level wanted is found iterate the tree
    while (length < level):

#start with empty list and the pervious level of the tree
      levels = []
      for elt in list[-1]:

#find all the roots from the previous nodes in the tree
        if (elt == None):
          continue
        else:
          levels.append(elt.lChild)
          levels.append(elt.rChild)

#add the list of children to main list
      list.append(levels)
      length = len(list)

#after wanted level is found, print the data out
    for item in list[level-1]:
      if item == None:
        pass
      else:
        print item.data,
    return ""

  # Returns the height of the tree
  def getHeight (self, node): 

#the null case of recursion
    if (node == None):
      return 0
    else:

#find the longer side of the two children using recursive
      if (self.getHeight(node.lChild) > self.getHeight(node.rChild)):
        return (self.getHeight(node.lChild) + 1)
      else:
        return (self.getHeight(node.rChild) + 1)

  def isBalanced(self):
    if self.root == None:
      return True
    else:
      return (self.getHeight(self.root.lChild) == self.getHeight(self.root.rChild))

  def isFull(self, aNode):
    if (aNode != None):
      self.isFull (aNode.lChild)
      if not self.isFull (aNode.lChild):
        return False
      if (aNode.lChild == None and aNode.rChild == None) or (aNode.lChild != None and aNode.rChild != None):
        if aNode.data == self.maximum().data:
          return True
      else:
        return False
      self.isFull (aNode.rChild)
      if not self.isFull (aNode.rChild):
        return False
    return True

  def isBinaryTree(self, aNode):
    if (aNode != None):
      self.isBinaryTree (aNode.lChild)
      if not self.isBinaryTree (aNode.lChild):
        return False
      if (aNode.lChild != None):
        if aNode.lChild.data > aNode.data:
          return False
      if (aNode.rChild != None):
        if aNode.rChild.data < aNode.data:
          return False
      if (aNode.lChild != None and aNode.rChild != None):     
        if (aNode.rChild.data < aNode.lChild.data):
          return False
      return True
      self.isBinaryTree (aNode.rChild)
      if not self.isBinaryTree (aNode.rChild):
        return False
    return True

def main():
    # Create three trees - two are the same and the third is different
  tree1 = Tree()
  tree2 = Tree()
  tree3 = Tree()
  tree4 = Tree()
  nums = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
  nums2 = [54, 45, 86, 2, 58, 42, 47, 3, 68, 65, 36, 78, 36, 87, 12]
  for elt in nums:
    tree1.insert(elt)
    tree2.insert(elt)
    tree4.insertMirror(elt)
  for item in nums2:
    tree3.insert(item)

  print tree1.isBinaryTree(tree1.root)
  print tree3.isBinaryTree(tree3.root)
  print tree4.isBinaryTree(tree4.root)

    # Test your method isSimilar()
  print  "\nSimilarity of two sets of trees"
  print "Tree 1 and Tree 2: " , tree1.isSimilar(tree2)
  print "Tree 1 and Tree 3: " , tree1.isSimilar(tree3)

    # Print the various levels of two of the trees that are different
  print  "\nLevel 3 of two different trees"
  print "Tree 1: " , tree1.printLevel(3)
  print "Tree 3: " , tree3.printLevel(3)

    # Get the height of the two trees that are different
  print  "\nHeights of two different trees"
  print "Tree 1: " , tree1.getHeight(tree1.root)
  print "Tree 3: " , tree3.getHeight(tree3.root)

main()