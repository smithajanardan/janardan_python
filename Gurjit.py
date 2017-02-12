  def isSimilar (self, pNode):

#same thing as printLevel but one for each list

    for loop (of list):
      for loop (nested loop)
        if either element in trees equals none:
          continue
        elif data form both nodes does not equal each other:
          return False
    return True

  def printLevel (self, level):

#suppose to use stacks, so i did it wrong here

#creating a 2D list of the tree. basically each inner 
#list will be the element at each level
#aka the list at list[4] will be the element of level 5

    if tree empty:
      return None
    create empty list 
    create empty list2
    add the root of tree to list 2
    add list2 to list
    find the length of the list
    while loop:
      create empty list2
      for loop (of last element in list):
        if element is none:
          continue
        else:
          add leftchild and righchild to the list2
      add list2 to list
      find the length of the list
    for loop (of the level):
      if item == None:
        pass
      else:
        print item.data,
    return

  def getHeight (self, node): 

#this is very unusual so ....
#recussion problem

    if the node is empty:
      return zero
    else:
      if getHeight(left side) is greater than getHeight(right side):
        return (getHeight(left side) + 1)
      else:
        return (getHeight(node.rChild) + 1)