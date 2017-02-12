#  File: ChatClient.py

#  Description: A client that can connect to other singles... i mean people... in the area.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398

#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 04/29/11

#  Date Last Modified: 05/06/11

#import necessary libraries
from socket import *
from threading import Thread

#set up the server connection
HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
server = socket (AF_INET, SOCK_STREAM)
server.connect (ADDRESS)

#object receiver: constantly recieves messages from server
class Receiver (Thread):

#default constructor to set to thread
  def __init__ (self):
    Thread.__init__(self, name = "Receiver")

#run function: receives messsages
  def run (self):

#in infinite loop:
    while True:

#recieve messages, if no message end program
      message = server.recv(BUFSIZE)
      if not message:
        print "server disconnected"
        break
      print "\n" + message

#object sender: sends messages to server
class Sender (Thread):

#default constructor: intiates the thread
  def __init__ (self):
    Thread.__init__(self , name = "Sender")

#run fucntion: sends messages to peeps
  def run (self):

#in infinite loop promp user for a message w/ no prompt
    while True:
      message = raw_input ("")

#if there is no message, break and crash
      if not message:
        print "server disconnected"
        break

#send the message to the server and disconnect
      server.send(message)
    server.close()

#main function: 
def main():

#prompt user to username and send to server
  name = raw_input("Enter your name: ")
  server.send(name)

#intiate all threads
  sender = Sender()
  receiver = Receiver()

#set sender thread to deamon so it closes when receiver closes
  sender.setDaemon(True)
  sender.start()
  receiver.start()

main()