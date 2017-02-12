#  File: ChatServer.py

#  Description: A server used to handle clients that wanna chat up others.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398

#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 04/29/11

#  Date Last Modified: 05/06/11

#import necessary libraries
from socket import *
from threading import Thread

#sendMessage function: sends the message to everyone but the sender
def sendMessage (string, sender):

#goes though list of clients and finds sender
  for client in clients:
    if client == sender:
      pass

#sends message to everyone else
    else:
      client.send(string)
  return

#object ClientHandler: creates a thread for each client
class ClientHandler (Thread):

#non-default constructor describes client
  def __init__ (self, id, client):
    Thread.__init__(self, name = id)
    self.client = client

#run fuction: sends and receives messages from client
  def run (self):

#send intial welcome message to client
    self.client.send("Welcome %s! To exit type bye." % self.getName())

#get the indivdual's name without the id number
    name = self.getName()
    name = name.split(':')
    name = name[0]

#tell everyone that the client has joined
    message = "\n%s has joined." % name
    sendMessage(message, self.client)

#in infinite loop:
    while True:

#get message from client
      message = self.client.recv(BUFSIZE)

#check if the message is bye close down client
      if (not message) or (message == "bye"):
        self.client.send("Thank you for using Chat Services")

#tell everyone that client has left
        message = "%s has left." % name
        sendMessage(message, self.client)

#close client and remove from client list
        self.client.close()
        clients.remove(self.client)
        break

#if there is a message, send to everyone
      else:
        message = name + " > " + message
        sendMessage(message, self.client)

#set up the server
HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
server = socket (AF_INET, SOCK_STREAM)
server.bind (ADDRESS)
server.listen (5)

#create globa variable of all clients
clients = []

#main function: creates thread for all new clients
def main():

#for the id number, finds the number fo clients in the list
  idNum = 0

#in infinite loop:
  while True:

#wait for a connection
    print 'Waiting for connection ...'

#when client connects, set-up the id, and create thread
    client, address = server.accept()
    print '... connected from:', address
    name = client.recv(BUFSIZE)
    id = name + ":" + str(idNum)

#add client to list of clients
    clients.append(client)
    numClients += 1
    handler = ClientHandler(id, client)
    handler.start()

main()