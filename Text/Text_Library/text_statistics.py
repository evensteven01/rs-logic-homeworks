# This module produces statistics about text
import ntk
import os
import json
import ast
import pickle

filename = "data.text"
filename2 = "data.json"

def getTotalParagraphsInText():
	num_of_paragraph = 0
	try:
		with open(filename, "r+") as text:
			for line in text.readlines():
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
			for line in file.readlines():
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
	num_of_characters = 0
	flag = True
	try:
		with open(filename, "r+") as file:
			while flag:
				characters = file.readlines()[1:]
				if not characters:
					break
				num_of_characters += len(characters)
			totalCharacters = sum(num_of_characters)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	finally:
		file.close()

def getTotalWords():
	num_of_words = 0
	try:
		with open(filename, "r+") as file:
			for line in file.readlines():
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