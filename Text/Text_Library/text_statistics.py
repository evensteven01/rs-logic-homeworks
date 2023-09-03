# This module produces statistics about text
import ntk
import os
import json
import ast
import pickle

filename = "data.text"
filename2 = "dictionary.text"

def getTotalParagraphsInText():
	num_of_paragraph = 0
	try:
		with open(filename, "r+") as text:
			for line in text:
				paragraph = line.split()
				num_of_paragraph += len(paragraph)
			totalParagraph = sum(num_of_paragraph)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	finally:
		text.close()

def getTotalParagraphsInFile():
	num_of_paragraph = 0
	try:
		with open(filename, "r+") as file:
			for line in file:
				paragraph = line.split()
				num_of_paragraph += len(paragraph)
			totalParagraph = sum(num_of_paragraph)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	finally:
		file.close()

def getTotalCharacters():
	pass

def getTotalWords():
	num_of_words = 0
	try:
		with open(filename, "r+") as file:
			for line in file:
				words = line.split()
				num_of_words += len(words)
			totalWords = sum(num_of_words)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	finally:
		file.close()

def getTotalSentences():
	pass

def getTotalCountsOfCertainCharacter():
	pass

def getTotalCountsOfListedCharacters():
	Dict = {}
	return dict.items(Dict)

def getTotalCountsOfListedWords(): 
	pass

def getAverageLengthOfWords():
	pass

def getAverageLengthOfSentences():
	pass

def getAverageNumbersOfSentencesPerParagraph():
	pass