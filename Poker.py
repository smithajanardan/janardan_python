#  File: Poker.py

#  Description: Simulate a 5-card poker game without betting.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 02/20/11

#  Date Last Modified: 02/22/11

#import necessary libraries
import random, string, math

#class Card that creates the object card that has a rank and suit
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('S', 'D', 'H', 'C')

  def __init__ (self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__ (self):
    if self.rank == 11:
      rank = 'J'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 14:
      rank = 'A'
    else:
      rank = self.rank
    return str(rank) + self.suit

#a function that compares one card to another
  def __cmp__ (self, other):
    if (self.rank < other.rank):
      return -1
    elif (self.rank > other.rank):
      return 1
    else:
      return 0

#object Deck with a deck of 52 cards (no jokers)
class Deck (object):

#non-default constructor of the deck
  def __init__(self):
    self.cards = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        c = Card(rank, suit)
        self.cards.append(c)

#shuffles the order of the cards
  def shuffle(self):
    random.shuffle(self.cards)

#deals first card if pile is not empty
  def deal(self):
    if len(self) == 0:
      return None
    else:
      return self.cards.pop(0)

#tells the length of the deck
  def __len__(self):
    return len(self.cards)

#returns the deck in string format
  def __str__(self):
    result = ""
    for c in self.cards:
      result = result + str(c) + "\n"
    return result

#object Poker that plays out the poker game
class Poker (object):

#non-default constructor to make n number of hands of poker
  def __init__ (self, numHands):
    self.deck = Deck()
    self.deck.shuffle()
    self.totalPoints = []
    self.hands = []
    numCards_in_Hand = 5

#creates the necessary number of hands
    for i in range (numHands):
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

#play function that plays the poker game and finds the winner
  def play(self):

#sorts each hand from lowest value to highest and prints the hand
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i])
      hand = ""
      for card in sortedHand:
        hand += str(card) + " "
      print "Hand " + str(i+1) + ": " + hand
    print

#puts each hand thought the functions to see which hand is possible
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i])
      if self.isRoyal(sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Royal Flush"
        self.totalPoints.append(self.isRoyal(sortedHand))
      elif self.isStraightFlush (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Stright Flush"
        self.totalPoints.append(self.isStraightFlush(sortedHand))
      elif self.isFour (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Four of a Kind"
        self.totalPoints.append(self.isFour(sortedHand))
      elif self.isFull (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Full House"
        self.totalPoints.append(self.isFull(sortedHand))
      elif self.isFlush (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Flush"
        self.totalPoints.append(self.isFlush(sortedHand))
      elif self.isStraight (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Straight"
        self.totalPoints.append(self.isStraight(sortedHand))
      elif self.isThree (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Three of a Kind"
        self.totalPoints.append(self.isThree(sortedHand))
      elif self.isTwo (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "Two Pairs"
        self.totalPoints.append(self.isTwo(sortedHand))
      elif self.isOne (sortedHand) > 0:
        print "Hand " + str(i+1) + ": " + "One Pair"
        self.totalPoints.append(self.isOne(sortedHand))
      else:
        print "Hand " + str(i+1) + ": " + "High Card"
        self.totalPoints.append(self.isHigh(sortedHand))

#finds the player with the highest number of points
    max = 0
    for elt in self.totalPoints:
      if elt > max:
        max =  elt
    winner = self.totalPoints.index(max)
    print

#adds a cause in case of a tie
    if self.totalPoints.count(max) == 1:
      print "Hand " + str(winner+1) + " wins."
    else:
      winner1 = self.totalPoints.index(max)
      winner2 = self.totalPoints.index(max, winner1)
      print "Hand " + str(winner1+1) + "and Hand" + str(winner2+1) + " wins."

#cheaks if hand is Royal Flush by confirming suit then first card is 10
  def isRoyal (self, hand):
    suit = hand[0].suit
    for h in hand:
      if h.suit != suit:
        return 0
    if hand[0].rank != 10:
        return 0
    else:
      return (10*(13**5)) + (hand[4].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[2].rank*(13**2)) + (hand[1].rank*13) + (hand[0].rank) 

#checks if hand is Straight Flush by confirming suit the consecutive numbers
  def isStraightFlush (self, hand):
    suit = hand[0].suit
    for h in hand:
      if h.suit != suit:
        return 0
    if (hand[4].rank - hand[0].rank) != 4:
      return 0
    else:
      return (9*(13**5)) + (hand[4].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[2].rank*(13**2)) + (hand[1].rank*13) + (hand[0].rank) 

#checks if hand is Four of a Kind by checking all possibilites
  def isFour (self, hand):
    if hand[1].rank == hand[4].rank:
      return (8*(13**5)) + (hand[1].rank*(13**4)) + (hand[2].rank*(13**3)) + (hand[3].rank*(13**2)) + (hand[4].rank*13) + (hand[0].rank) 
    elif hand[0].rank == hand[3].rank:
      return (8*(13**5)) + (hand[0].rank*(13**4)) + (hand[1].rank*(13**3)) + (hand[2].rank*(13**2)) + (hand[3].rank*13) + (hand[4].rank) 
    else:
      return 0

#checks if hand is full house by checking all possibilites 
  def isFull (self, hand):
    if hand[0].rank == hand[2].rank and hand[3].rank == hand[4].rank:
      return (7*(13**5)) + (hand[0].rank*(13**4)) + (hand[1].rank*(13**3)) + (hand[2].rank*(13**2)) + (hand[3].rank*13) + (hand[4].rank) 
    elif hand[0].rank == hand[1].rank and hand[2].rank == hand[4].rank:
      return (7*(13**5)) + (hand[2].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[4].rank*(13**2)) + (hand[0].rank*13) + (hand[1].rank) 
    else:
      return 0

#checks if hand is Flush by confirming suit
  def isFlush (self, hand):
    suit = hand[0].suit
    for h in hand:
      if h.suit != suit:
        return 0
    return (6*(13**5)) + (hand[4].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[2].rank*(13**2)) + (hand[1].rank*13) + (hand[0].rank) 

#checks if hand is Striaght by checking consecutive numbers
  def isStraight (self, hand):
    for i in range(len(hand)-1):
      if hand[i].rank != (hand[i+1].rank - 1):
        return 0
    else:
      return (5*(13**5)) + (hand[4].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[2].rank*(13**2)) + (hand[1].rank*13) + (hand[0].rank) 

#checks if hand is Three of a Kind by having a count and adding to it
  def isThree (self, hand):
    match = hand[2].rank
    count = 0
    other = []
    for card in hand:
      if card.rank == match:
        count += 1
      else:
        other.append(card.rank)
    if count == 3:
       return (4*(13**5)) + (match*(13**4)) + (match*(13**3)) + (match*(13**2)) + (other[1]*13) + (other[0]) 
    else:
      return 0

#checkes if hand is Two Pairs by checking all possibilites
  def isTwo (self, hand):
    if hand[1].rank == hand[0].rank:
      if hand[3].rank == hand[2].rank:
        return (3*(13**5)) + (hand[3].rank*(13**4)) + (hand[2].rank*(13**3)) + (hand[1].rank*(13**2)) + (hand[0].rank*13) + hand[4].rank
      elif hand[3].rank == hand[4].rank:
        return (3*(13**5)) + (hand[4].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[1].rank*(13**2)) + (hand[0].rank*13) + hand[2].rank
      else:
        return 0
    elif hand[1].rank == hand[2].rank:
      if hand[3].rank == hand[4].rank:
        return (3*(13**5)) + (hand[4].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[1].rank*(13**2)) + (hand[2].rank*13) + hand[0].rank
      else:
        return 0
    else:
      return 0

#Checks if hand is One Pair by checking all possibilites 
  def isOne (self, hand):
    if hand[1].rank == hand[0].rank:
      return (2*(13**5)) + (hand[1].rank*(13**4)) +(hand[0].rank*(13**3)) +(hand[4].rank*(13**2)) +(hand[3].rank*13) + hand[2].rank
    elif hand[1].rank == hand[2].rank:
      return (2*(13**5)) + (hand[1].rank*(13**4)) +(hand[2].rank*(13**3)) +(hand[4].rank*(13**2)) +(hand[3].rank*13) + hand[0].rank
    elif hand[3].rank == hand[2].rank:
      return (2*(13**5)) + (hand[3].rank*(13**4)) +(hand[2].rank*(13**3)) +(hand[4].rank*(13**2)) +(hand[1].rank*13) + hand[0].rank
    elif hand[3].rank == hand[4].rank:
      return (2*(13**5)) + (hand[3].rank*(13**4)) +(hand[4].rank*(13**3)) +(hand[2].rank*(13**2)) +(hand[1].rank*13) + hand[0].rank
    else:
      return 0

#finds the highest card in the hand
  def isHigh (self, hand):
    return (13**5) + (hand[4].rank*(13**4)) + (hand[3].rank*(13**3)) + (hand[2].rank*(13**2)) + (hand[1].rank*13) + hand[0].rank

#Returns the hands in string format
  def __str__ (self):
    result = ""
    for c in self.hands:
      for d in c:
        result += str(d) + " "
      result += "\n"
    return result

#main function: ask number of hands. input: number of hands (2-6). output: hands and winner
def main():
  hands = input("Enter the number of hands to play: ")

#makes sure number of hands is within set range
  while hands not in range (2,7):
    print "Error: Number of hands is not between 2 to 6"
    hands = input("Enter the number of hands to play: ")

#play the poker game
  game = Poker(hands)
  print
  game.play()

main()