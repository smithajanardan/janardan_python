#  File: TestGraph.py

#  Description: Order the vertices visited when transversing a graph depth first and breath first

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 313E

#  Unique Number: 53330

#  Date Created: 04/10/11

#  Date Last Modified: 04/15/11

# = functions in book
## = other stuff Dr. Mitra put in here
### = written functions

class Vertex (object):
  # creates a vertex with specific label 
  # and the vertex is initially unmarked
  def __init__ (self, label):
    self.label = label
    self.edgeList = []
    self.mark = False

  # unmark the vertex
  def clearMark (self):
    self.mark = False

  # mark the vertex
  def setMark (self):
    self.mark = True

  ### returns True if the vertex is marked and False otherwise
  def isMarked (self):
    return self.mark

  ### returns the label of the vertex
  def getLabel (self):
    return self.label

  # changes the label of the vertex in the graph g to given label
  def setLabel (self, label, g):
    g.vertices.pop (self.label, None)
    g.vertices[label] = self
    self.label = label

  # adds an edge with the given weight from this vertex to the toVertex
  def addEdgeTo (self, toVertex, weight = 1):
    edge = Edge(self, toVertex, weight)
    if edge in self.edgeList:
      return False
    else:
      self.edgeList.append(edge)

  ### returns the edge from this vertex to the toVertex or 
  ### returns None if the edge does not exist
  def getEdgeTo (self, toVertex):
    for item in self.edgeList:

      #check if each edge has the toVertex as a destination
      if (item.vertex2 == toVertex):
        return item

    #return none is no edge is found
    return None

  ### returns a list of the incident edges of this vertex
  def incidentEdges (self):
    list = []

    #tranverse edges and create a copy of each
    for item in self.edgeList:
      edge = Edge(item.vertex1, item.vertex2, item.weight)
      list.append(edge)

    #return new list that will not effect graph
    return list

  # returns a list of vertices that are adjacent to this vertex
  def neighboringVertices (self):
    vertices = []
    for edges in self.edgeList:
      vertices.append(edge.getOtherVertex(self))
    return iter(vertices)

  # removes the edge leading to a given vertex
  def removeEdgeTo(self, toVertex):
    edge = Edge(self, toVertex)
    if edge in self.edgeList:
      self.edgeList.remove(edge)
      return True
    else:
      return False

  ### returns a string representation of the vertex
  def __str__ (self):
    return str(self.label)

class Edge (object):
  # creates an edge with specified vertices and weight
  # it is inially unmarked
  def __init__ (self, fromVertex, toVertex, weight = 1):
    self.vertex1 = fromVertex
    self.vertex2 = toVertex
    self.weight = weight
    self.mark = False

  ### unmarks the edge
  def clearMark (self):
    self.mark = False

  ### marks the edge 
  def setMark (self):
    self.mark = True

  ### returns True if the edge is marked and False otherwise
  def isMarked (self):
    return self.mark

  ### returns the weight of the edge
  def getWeight (self):
    return self.weight

  ### sets the edge's weight
  def setWeight (self, weight):
    self.weight = weight

  ### returns the edge's other vertex
  def getOtherVertex (self, vertex):

    #if the vertex is the beginning return the end
    if vertex == self.vertex1:
      return self.vertex2

    #if the vertex is the end return the beginning
    else:
      return self.vertex1

  ### returns the edge's destination vertex
  def getToVertex (self):
    return self.vertex2

  ### returns the string representation of the edge
  def __str__(self):
    return str(self.vertex1) + " " + str(self.vertex2) + " " + str(self.weight)

class Graph (object):
  # creates a graph with adjacency list
  def __init__ (self, collection = None):
    self.vertexCount = 0
    self.edgeCount = 0
    self.vertices = {}
    if collection != None:
      for label in collection:
        self.addVertex(label)

  ### removes all vertices and edges from the graph
  def clear (self):

    #empty everything
    self.vertices = {}
    self.edgeCount = 0
    self.vertexCount = 0

  ### unmark all vertices
  def clearVertexMarks (self):
    for item in self.vertices.values():
      item.clearMark()

  ### unmark all edges
  def clearEdgeMarks (self):
    for elt in self.edges():
      elt.mark = False

  ### returns True if the graph is empty and False otherwise
  def isEmpty (self):
    return (self.vertexCount == 0) and (self.edgeCount == 0)

  ### returns the number of edges in the graph
  def numEdges (self):
    return self.edgeCount

  ### returns the number of vertices in the graph
  def numVertices (self):
    return self.vertexCount

  ### returns the String representation of the graph
  def __str__ (self):
    print "\nVertices: "
    for item in self.vertices.keys():
      print str(item)
    print "\nEdges (From, To, Weight): "
    for elt in self.edges():
      print elt
    return ""

  ## vertex related functions ##

  ### returns True if the graph contains this vertex and False otherwise
  def containsVertex (self, label):

    #transverse the keys in the dictionary looking for label
    for item in self.vertices.keys():
      if item == label:
        return True
    return False

  # adds a vertex with the specified label
  def addVertex (self, label):
    self.vertices[label] = Vertex(label)
    self.vertexCount += 1

  ### returns the vertex with the label or None
  def getVertex (self, label):

    #transverse the keys in the dictionary looking for label
    for item in self.vertices.keys():
      if item == label:
        return self.vertices[item]
    return None

  # removes the vertex with the label
  def removeVertex (self, label):
    removedVertex = self.vertices.pop(label, None)
    if removedVertex is None:
      return False
    for vertex in self.vertices():
      if vertex.removeEdgeTO(removeVertex):
        self.edgeCount -= 1
    self.vertexCount -= 1
    return True

  ## edge related functions ##

  ### returns True if the graph contains this edge and False otherwise
  def containsEdge (self, fromLabel, toLabel):

    #find the actual vertices given the labels
    fromVertex = self.vertices[fromLabel]
    toVertex = self.vertices[toLabel]

    #transverse edge list looking for a match
    for item in fromvertex.edgeList:
      if item.vertex2 == toVertex:
        return True
    return False

  # adds an edge with given weight
  def addEdge (self, fromLabel, toLabel, weight = 1):
    fromVertex = self.getVertex(fromLabel)
    toVertex = self.getVertex(toLabel)
    fromVertex.addEdgeTo(toVertex, weight)
    self.edgeCount += 1

  # returns the edge or None
  def getEdge (self, fromLabel, toLabel):
    fromVertex = self.vertices[fromLabel]
    toVertex = self.vertices[toLabel]
    return fromVertex.getedgeTo(toVertex)

  # remove and return the edge
  def removeEdge (self, fromLabel, toLabel):
    fromVertex = self.getVertex[fromLabel]
    toVertex = self.vertices[toLabel]
    return fromVertex.getEdgeTo(toVertex)

  ## iterators  ##

  # returns a list of edges in the graph
  def edges (self):
    result = set()
    for vertex in self.vertices.keys():
      edges = self.incidentEdges(vertex)
      result = result.union(set(edges))
    return iter(result)

  ### returns a list of vertices in the graph
  def vertices (self):

    #make a new list
    list = []

    #add vertices to the list
    for item in self.vertices.values():
      list.append(item)
    return list

  ### returns the list of edges from a given vertex
  def incidentEdges (self, label):

    #find the vertex object and create a list
    vertex = self.vertices[label]
    edgeList = []

    #transverse the edges, create copies, and add to the list
    for item in vertex.edgeList:
      edge = Edge(item.vertex1, item.vertex2, item.weight)
      edgeList.append(edge)
    return edgeList

  ### returns the list of vertices adjacent to a given vertex
  def neighboringVertices (self, label):

    #find the vertex object and create a list 
    vertex = self.vertices[label]
    vertexList = []

    #transverse the edges, find other vertex, and add to the list
    for item in vertex.edgeList:
      vertice = item.vertex2
      vertexList.append(vertice)
    return vertexList

  ### prints a list of vertices when transversing a graph depth first
  def depthFirstSearch (self, startLabel):

    #initiate stacks and queues, and clear graph
    self.clearVertexMarks()
    queue = Queue ()
    stack = Stack ()

    #start transveral from the given vertex
    startVertex = self.vertices[startLabel]
    queue.enqueue(startVertex)

    #add all the neighbooring vertices to the stack
    for elt in startVertex.edgeList:
      stack.push(elt.vertex2)

    #create boolean to stop while loop
    bool = stack.isEmpty()
    while bool != True:

      #take the first item off of the stack
      vertex = stack.pop()

      #if the vertex is visited move on, otherwise visit it
      if vertex.isMarked():
        pass
      else:
        vertex.setMark()
        queue.enqueue(vertex)

        #find all neightbooring vertices and add to stack
        for elt in vertex.edgeList:
          if elt.vertex2.isMarked():
            pass
          elif elt.vertex2.label == startLabel:
            pass
          else:
            stack.push(elt.vertex2)

      #make sure that the stack isn't empty
      bool = stack.isEmpty()

    #print visited vertices using string formatting
    print "\nDepth First Traversal"
    while (queue.size() >= 5):
      for i in range (5):
        print str(queue.dequeue()).center(3),
      print ""
    for i in range (queue.size()):
      print str(queue.dequeue()).center(3),
    return ""

  ### prints a list of vertices when transversing a graph breath first
  def breathFirstSearch (self, startLabel):

    #use same method as depth first with two queues instead of a stack
    self.clearVertexMarks()
    queue = Queue ()
    queue2 = Queue ()
    startVertex = self.vertices[startLabel]
    queue2.enqueue(startVertex)
    for elt in startVertex.edgeList:
      queue.enqueue(elt.vertex2)
    bool = queue.isEmpty()
    while bool != True:
      vertex = queue.dequeue()
      if vertex.isMarked():
        pass
      else:
        vertex.setMark()
        queue2.enqueue(vertex)
        for elt in vertex.edgeList:
          if elt.vertex2.isMarked():
            pass
          elif elt.vertex2.label == startLabel:
            pass
          else:
            queue.enqueue(elt.vertex2)
      bool = queue.isEmpty()
    print "\nBreadth First Traversal"
    while (queue2.size() >= 5):
      for i in range (5):
        print str(queue2.dequeue()).center(3),
      print ""
    for i in range (queue2.size()):
      print str(queue2.dequeue()).center(3),
    return ""

  def breathFirstCount (self, startLabel):
    self.clearVertexMarks()
    queue = Queue ()
    count = 0
    startVertex = self.vertices[startLabel]
    for elt in startVertex.edgeList:
      queue.enqueue(elt.vertex2)
    bool = queue.isEmpty()
    while bool != True:
      vertex = queue.dequeue()
      if vertex.isMarked():
        pass
      else:
        vertex.setMark()
        count += 1
        for elt in vertex.edgeList:
          if elt.vertex2.isMarked():
            pass
          elif elt.vertex2.label == startLabel:
            pass
          else:
            queue.enqueue(elt.vertex2)
      bool = queue.isEmpty()
    return count

  def greatest(self):
    list = []
    max = 0
    for item in self.vertices.values():
      num = self.breathFirstCount(item.label)
      if num > max:
        list = []
        list.append(item.label)
        max = num
      elif num == max:
        list.append(item.label)
    return list

class Stack (object):
  # create a stack object using a list
  def __init__ (self):
    self.stack = []

  # push an object on the stack
  def push (self, data):
    self.stack.append (data)

  # pop an object off the stack
  def pop (self):
    return self.stack.pop()

  # peek at an object on the top of the stack
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # return True if the Stack is empty or False otherwise
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of objects in the Stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  # create a queue object using a list
  def __init__ (self):
    self.queue = []

  # add an object from the queue
  def enqueue (self, data):
    self.queue.append (data)

  # remove an object from the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # return True if the Queue is empty or False otherwise
  def isEmpty (self):
    return (len (self.queue) == 0)

  # return the number of objects in the Queue
  def size (self):
    return len (self.queue)

def main():

  #open the output file
  input = open ("graph.txt", "r")

  #find the number of vertices and edges
  ve = input.readline().rstrip("\n").split()
  v = int(ve[0])
  e = int(ve[1])

  #transverse the file to find all vertices
  vertices = []
  while v > 0:
    vertex = int(input.readline().rstrip("\n"))
    vertices.append(vertex)
    v -= 1

  # create the graph using vertices
  graph = Graph(vertices)

  #transverse the file to find all edges 
  while e > 0:
    edge = input.readline().rstrip("\n").split()

    #add each edge to the graph
    if len(edge) == 2:
      graph.addEdge(int(edge[0]),int(edge[1]))
    elif len(edge) == 3:
      graph.addEdge(int(edge[0]),int(edge[1]),int(edge[2])) 
    else:
      print "Error: Given edges/vertices are not valid"
    e -= 1

  #find the starting vertex
  start = input.readline()

  #close the output
  input.close()

  # find depthFirstSearch and breathFirstSearch
  print graph.depthFirstSearch(int(start))
  print graph.breathFirstSearch(int(start))

  print graph.greatest()

main()