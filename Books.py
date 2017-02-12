#  File: Books.py

#  Description: Compares the vocabulary in two books.

#  Student Name: Smitha Janardan

#  Student UT EID: ssj398

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 11/19/10

#  Date Last Modified: 11/29/10

import string

# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
  words = open("words.txt", "r")
  for line in words:
    word_dict[line] = 1
  words.close()
  return

# Removes punctuation marks from a string
def parseString (st):
  st = st.replace("\n"," ")

#creating a new string and only adding letters and spaces to it
  str = ""
  for ch in st:
    if ch == "-":
      str += " "
    if ch.isalpha() or ch.isspace():
      str += ch
    else:
      str += " "
  return str

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  input = open (file, "r")
  book = {}

#removing all necessary characters in book
  for line in input:
    line = line.rstrip("\n")
    line = parseString(line)

#moving string into a dictionary
    line = line.split()

#getting word frequencies in the dictionary.
    for elt in line:
      if elt in book:
        book[elt] += 1
      else:
        book[elt] = 1
  input.close()

#opening the list of dictionary words
  dele = []
  thing = book.keys()

#check for proper nouns
  for key in thing:
    if key[0].isupper():
      if key.lower() in book:
        book[key.lower()] += book[key]
      elif key.lower() in word_dict:
        book[key.lower()] = book[key]
      dele.append(key)

#deleting proper nouns
  for item in dele:
    del book[item]
  return book
  
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
  print author1
  print "Total distinct words = ", len(freq1)

#finding the total words used by author one
  sum = 0
  for key in freq1.values():
    sum += key
  sum = float(sum)

#printing everything for author one
  print "Total words (including duplicates) = ", int(sum)
  print "Ratio(% of total distinct words to total words) = ", (len(freq1)/sum)*100
  print
  print author2
  print "Total distinct words = ", len(freq2)

#finding the total words used by author two
  sum2 = 0
  for key in freq2.values():
    sum2 += key
  sum2 = float(sum2)

#printing everything for author two
  print "Total words (including duplicates) =", int(sum2)
  print "Ratio(% of total distinct words to total words) = ", (len(freq2)/sum2)*100
  print
  book1 = set(freq1.keys())
  book2 = set(freq2.keys())

#printing cross comparisons
  print "%s used %d words that %s did not use." % (author1, len(book1-book2), author2)
  print "Relative frequency of words used by %s not in common with %s = %f" % (author1, author2, (len(book1-book2)/sum)*100)
  print
  print "%s used %d words that %s did not use." % (author2, len(book2-book1), author1)
  print "Relative frequency of words used by %s not in common with %s = %f" % (author2, author1, (len(book2-book1)/sum2)*100)
  return

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = raw_input ("Enter name of first book: ")
  book2 = raw_input ("Enter name of second book: ")
  print

  # Enter names of the two authors
  author1 = raw_input ("Enter last name of first author: ")
  author2 = raw_input ("Enter last name of second author: ")
  print 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
