#  File: TestCipher.py

#  Description: Takes a string as input and codes/decodes it using two different methods.

#  Student's Name: Smitha Janardan

#  Student's UT EID: ssj398
 
#  Course Name: CS 313E 

#  Unique Number: 53330

#  Date Created: 02/09/11

#  Date Last Modified: 02/09/11

#substitution_encode function: encodes a string using first method. input: string. output: coded string
def substitution_encode ( strng ):
  cipher = [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p' ]
  code = ""
  for letter in strng:

#skips everything but letters
    if not letter.isalpha():
      code += letter

#uses formula to encode
    else:
      idx = ord(letter.lower()) - ord('a')
      code += cipher[idx]
  return code

#substitution_decode function: decodes a string using first menthod. input: coded string. output: string
def substitution_decode ( strng ):
  cipher = [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p' ]
  code = ""
  for letter in strng:

#skips everything but letters
    if not letter.isalpha():
      code += letter

#uses reverse formula to decode
    else:
      idx = cipher.index(letter.lower()) + ord('a')
      code += chr(idx)
  return code

#vigenere_encode function: encodes a string using second method. input: string, pass phrase. output: coded string
def vigenere_encode ( strng, passwd ):
  idx = 0
  code = ""
  for letter in strng:

#skips everything but letters
    if not letter.isalpha():
      code += letter
      continue

#uses formula to find enocoded letter
    else:
      letter = ord(letter.lower()) + ord(passwd[idx]) -97
      if letter > 122:
        letter += -26
      code += chr(letter)

#changes index of pass phrase
    idx += 1
    if idx == len(passwd):
      idx += -len(passwd)
  return code

#vigenere_decode function: decodes a string using second method. input: coded string, pass phrase. output: string
def vigenere_decode ( strng, passwd ):
  idx = 0
  code = ""
  for letter in strng:

#skips everything but letters
    if not letter.isalpha():
      code += letter
      continue
    else:

#uses reverse formula to decode each letter
      letter = ord(letter.lower()) - ord(passwd[idx]) +97
      if letter < 97:
        letter += 26
      code += chr(letter)

#changes index of pass phrase
    idx += 1
    if idx == len(passwd):
      idx += -len(passwd)
  return code

#main function: print input statements, print output statements. input: strings, coded strings, pass phrase. output: strings, coded strings
def main():
  print "\n", "Substitution Cipher", "\n"
  subEnText = raw_input("Enter Plain Text to be Encoded: ")
  print "Encoded Text: ", substitution_encode (subEnText), "\n"
  subDeText = raw_input("Enter Encoded Text to be Decoded: ")
  print "Decoded Plain Text: ", substitution_decode (subDeText), "\n"
  print "Vigenere Cipher", "\n"
  vigEnText = raw_input("Enter Plain Text to be Encoded: ")
  vigEnPass = raw_input("Enter Pass Phrase (no spaces allowed): ")
  print "Encoded Text: ", vigenere_encode (vigEnText, vigEnPass), "\n"
  vigDeText = raw_input("Enter Encoded Text to be Decoded: ")
  vigDePass = raw_input("Enter Pass Phrase (no spaces allowed): ")
  print "Decoded Plain Text: ", vigenere_decode (vigDeText, vigDePass)

main()
