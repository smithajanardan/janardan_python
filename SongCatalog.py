#  File: SongCatalog.py

#  Description: A menu of options to alter a catalog of song names/artists.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 02/28/11

#  Date Last Modified: 03/03/11

#class SongCatalog: menu of options to alter cataog
class SongCatalog (object):

#default constuctor that create a dictionary of each artist and thier keys
  def __init__ (self):
    infile = open("songs.txt", "r")

#creates an empty dictionary to add too
    self.songs = {}

#line by line, reads the file and adds it to the dictionary
    while True:
      artist = infile.readline().rstrip("\n")
      title = infile.readline().rstrip("\n")
      line = infile.readline()
      if artist == "":
        break

#adds only the song if the artist is already in the dictionary
      elif artist[8:] in self.songs:
        self.songs[artist[8:]].append(title[7:])
      else:
        self.songs[artist[8:]] = [title[7:]]
    infile.close()
    self.menu()

#menu function: displays the menu and calls the individual functions.
  def menu(self):
    print "\nSong Catalog Menu\n\n1. Import songs from a file\n\n2.\
 Add a song\n\n3. Delete a song\n\n4. Search for a song\n\n5.\
 Display all songs\n\n6. Exit program\n"
    selection = input("Enter selection (1 - 6): ")

#makes suere the selection choice is one of the given choices
    while selection not in range (1,7):
      selection = input("Enter selection (1 - 6): ")

#depending on the selection chioce, will ask for addition info and run a function
    if selection == 1:
      fileName = raw_input("\nPlease enter the name of .txt file with path: ")
      self.readFile(fileName)
    elif selection == 2:
      print "\nAdd a Song"
      artist = raw_input("\nEnter artist: ")
      title = raw_input("\nEnter title: ")
      self.addSong(artist,title)
    elif selection == 3:
      print "\nDelete a Song"
      artist = raw_input("\nEnter artist: ")
      title = raw_input("\nEnter title: ")
      self.deleteSong(artist,title)
    elif selection == 4:
      print "\nSearch for an Artist / Song"
      artist = raw_input("\nEnter artist: ")
      title = raw_input("\nEnter title: ")
      self.searchCatalog(artist,title)
    elif selection == 5:
      self.displayCatalog()
    else:
      self.saveFile()

#given song information, will add the song to the catalog
  def addSong (self, artist, title):

#if no information is given, will return to menu
    if artist == "" or title == "":
      self.menu()

#if song is already there, tells user as such
    if self.search(artist, title) == True:
      print "Error: Song already present in catalog"
      self.menu()  

#adds the song to the dictionary catalog
    elif self.search(artist, title) == artist:
      self.songs[artist].append(title)
      self.menu()
    self.songs[artist] = [title]
    self.menu()

#given song name or artist, will delete the items form the catalog
  def deleteSong (self, artist, title):

#If no information given returns to menu
    if artist == "" and title == "":
      print "\nError: No artist name given. No song name given."
      self.menu()

#If only artist is given, deletes entire artist
    elif self.search(artist, title) == artist and title == "":
      confirm = raw_input("\nAre you sure you wish to delete all songs by this artist? [y/n]: ")
      if confirm == 'y' or confirm == 'Y':
        del self.songs[artist]
      self.menu()

#If onlt title is given, deletes all songs by this title
    elif self.search(artist, title) == title and artist == "":
      confirm = raw_input("\nAre you sure you wish to delete all songs by this name? [y/n]: ")
      if confirm == 'y' or confirm == 'Y':
        for key in self.songs:
          if title in self.songs.key:
            self.songs[key].remove(title)
      self.menu()

#if song and artist are present, removes form the catalog
    elif self.search(artist, title) == True:
      confirm = raw_input("\nAre you sure you wish to delete this song? [y/n]: ")
      if confirm == 'y' or confirm == 'Y':
        self.songs[artist].remove(title)
      self.menu()

#in all other cases, returns to menu
    else:
      print "\nError: Song specified not present in catalog"
      self.menu()

#given song info, will search for any matches in the catalog
  def search (self, artist, title):

#start with a boolean
    confirm = False

#linear search through the catalog for artist match
    for key in self.songs:

#if both song title and artist found, returns true
      if key == artist and title in self.songs[key]:
        confirm = True
        return confirm

#if only artist found, returns artist's name
      elif key == artist:
        confirm = artist
        return confirm

#if only title found, returns title
      elif title in self.songs[key]:
        confirm = title

#in all other cases, returns false
    return confirm

#given the song info, will tell the user if the song is present
  def searchCatalog (self, artist, title):

#if if both song title and artist found, prints as such
    if self.search(artist, title) == True:
      print "Song/Artist found in catalog"
      self.menu()

#if only artist found, prints all songs by artist
    elif self.search(artist, title) == artist and title == "":
      print "\nSongs: ",
      for elt in self.songs[artist]:
        print elt, ",",
      self.menu()

#if only title found, prints all artist's names
    elif self.search(artist, title) == title and artist == "":
      print "\nArtist: ",
      for key in self.songs:
        if title in self.songs[key]:
          print key, ",",
      self.menu()

#in all other cases, prints song/artist not found
    else:
      print "Error: Artist/Song not in catalog"
      self.menu()

#displays the current catalog in alphabetical order
  def displayCatalog (self):

#turns the dictionary into a list of tuples
    list = self.songs.items()

#sorts list by artist's names
    sortedList = sorted(list, key=lambda artist: artist[0].lower())

#sorts songs alphabetically
    for elt in sortedList:
      artist, songs = elt
      songs.sort()
      for item in songs:

#prints all artists and songs for user
        print "\nArtist: ", artist, "\nTitle: ", item
    self.menu()

#creates a dictionary of songs from a file other than songs.txt 
  def readFile (self, fileName):

#tests to see if filename exists and is readable
    try:
      infile = open(fileName, "r")
    except IOError:
      print "\nError: File name and/or path does fit criteria"
      self.menu()

#creates a dictionary from the information in the file (same method as __init__)
    while True:
      artist = infile.readline().rstrip("\n")
      title = infile.readline().rstrip("\n")
      line = infile.readline()
      if artist == "":
        break
      elif artist[8:] in self.songs:
        self.songs[artist[8:]].append(title[7:])
      else:
        self.songs[artist[8:]] = [title[7:]]
    infile.close()
    self.menu()

#writes the catalog to songs.txt in alphabetical order
  def saveFile (self):

#creats a list of tuples
    list = self.songs.items()

#sorts the list
    sortedList = sorted(list, key=lambda artist: artist[0].lower())
    outfile = open("songs.txt", "w")

#sorts the songs
    for elt in sortedList:
      artist, songs = elt
      songs.sort()
      for item in songs:

#writes everything into an output file
        outfile.write("Artist: " + artist + "\nTitle: " + item + "\n\n")
    outfile.close()
    return

#main function: initiates the class SongCatalog.
def main():
  program = SongCatalog()

main()