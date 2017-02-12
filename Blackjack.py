#  File: Blackjack.py

#  Description: Simulate a game of blackjack.
#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 02/14/11

#  Date Last Modified: 02/17/11

import random

#the object Card that has a rank and a suit
class Card (object):

  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

#non-default constructor of the card
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

#returns a string version of the card
  def __str__(self):
    if self.rank == 1:
      rank = "Ace"
    elif self.rank == 11:
      rank = "Jack"
    elif self.rank == 12:
      rank = "Queen"
    elif self.rank == 13:
      rank = "King"
    else:
      rank = self.rank
    return str(rank) + " of " + self.suit.lower()

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

#Oject Player creates the player's hand
class Player (object):

#non-default constructor to player's hand
  def __init__ (self, cards):
    self.cards = cards

#returns string version of cards in hand
  def __str__ (self):
    result = ", ".join(map(str, self.cards))
    result += "\n " + str(self.getPoints()) + " points"
    return result

#adds more cards to hand
  def hit(self, card):
    self.cards.append(card)

#counts the number of points the player's hand
  def getPoints(self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count -= 10
    return count

#determines weather the player has 21 points or not
  def hasBlackjack(self):
    return len(self.cards) == 2 and self.getPoints() == 21

#object Dealer creates the dealer of the deck
class Dealer (Player):

#non-default constructor of the dealer
  def __init__ (self, cards):
    Player.__init__(self, cards)
    self.showOneCard = True

#returns string version of the dealer
  def __str__ (self):
    if self.showOneCard:
      return str(self.cards[0])
    else:
      return Player.__str__(self)

#Add cards untill point equal 17 and then show cards
  def hit(self, deck):
    self.showOneCard = False
    while self.getPoints() < 17:
      self.cards.append(deck.deal())

#object Blackjack simulates the blackjack game
class Blackjack (object):

#default constructor of the blackjack game
  def __init__ (self):
    self.deck = Deck()
    self.deck.shuffle()
    self.player = Player([self.deck.deal(), self.deck.deal()])
    self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

#plays the blackjack game out
  def play(self):
    print "Player:\n", self.player
    print "Dealer:\n", self.dealer

#gives player has many cards necessary
    while True:
      choice =  raw_input("Do you want a hit? [y/n]: ")
      if choice in ("Y", "y"):
        self.player.hit(self.deck.deal())
        points = self.player.getPoints()
        print "Player:\n", self.player
        if points >= 21:
          break
      else:
        break
    playerPoints = self.player.getPoints()
    if playerPoints > 21:
      print "You bust and lose"

#gives the dealer more cards if necessary
    else:
      self.dealer.hit(self.deck)
      print "Dealer:\n", self.dealer.getPoints()
      dealerPoints = self.dealer.getPoints()

#determines final outcome
      if dealerPoints > 21:
        print "Dealer Busts and you win"
      elif dealerPoints > playerPoints:
        print "Dealer wins"
      elif dealerPoints < playerPoints and playerPoints <= 21:
        print "You win"
      elif dealerPoints == playerPoints:
        if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
          print "You win"
        elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
          print "Dealer wins"
        else:
          print "There is a tie"

def main():
  game = Blackjack()
  game.play()

main()