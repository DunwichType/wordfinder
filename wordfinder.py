#!/usr/bin/env python -B
# -*- coding: utf-8 -*-

# wordfinder v.0.03
# wordfinder originated by James Puckett of Dunwich Type Founders

# wordfinder is licensed under the Apache License:
# https://www.apache.org/licenses/LICENSE-2.0

# wordfinder can be downloaded at github.com/DunwichType

# wordfinder is a tool for generating lists of words containing letters 
# pulled from a list. It can words containing a specified letter at 
# the beginning, middle, or end of a word.

# regular expression module is needed for pattern matching
import re
# codecs module is needed to work with non-ascii files
import codecs

# open the word list and read it into lines
wordList = codecs.open('wordList.txt', 'r', 'utf-8')
lines = wordList.readlines()

# open the character list and read it into charList
charList = codecs.open('charList.txt', 'r', 'utf-8')
characters = charList.readlines()

# search at the beginning of words
def searchBegin (searchChar):
	regex = searchChar
	regex += '.{1,7}'
	pattern = re.compile(regex)
	for (offset, line) in enumerate(lines):
		if re.match(pattern, line):
			return line
			break
		else:
			pass
	return 'none'
			
# search inside of words		
def searchMiddle (searchChar):
	regex = '.{2,3}' + searchChar + '.{2,3}'
	pattern = re.compile(regex)
	for (offset, line) in enumerate(lines):
		if re.match(pattern, line):
			return line
			break
		else:
			pass
	return 'none'
			
# search at the end of words				
def searchEnd (searchChar):
	regex = '.{1,7}'
	regex += searchChar
	regex += '$'
	pattern = re.compile(regex)
	for (offset, line) in enumerate(lines):
		if re.match(pattern, line):
			return line
			break
		else:
			pass
	return 'none'
	
#outputter creates the file we output text to
def outputter (title):
	global output
	output = open( title+'.txt', 'w')
	output.write
	output.write ( "Found Words")
	output.write( '\n')

#Now do the work
outputter ("foundwords")
		
for (offset, searchChar) in enumerate(characters):
	first = searchBegin (searchChar.strip())
	second = searchMiddle (searchChar.strip())
	third = searchEnd (searchChar.strip())
	foundLine = searchChar.strip() +' '+ first.strip() +' '+ second.strip()  +' '+ third.strip()+'\n'
	output.write(foundLine.encode( "utf-8" ))

	