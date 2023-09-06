# This module produces statistics about text
import ntk
import os
import json
import ast
import pickle

filename = "data.text"
filename2 = "data.json"

# this function will gets the total of paragraph
def getTotalParagraphsInText(text: str)-> int:
	num_of_paragraph = 0

	if text is None:
		return num_of_paragraph

	for line in text.split("\n"):
		num_of_paragraph += len(line)
	totalParagraph = sum(num_of_paragraph)
	return totalParagraph

def getTotalParagraphsInFile(file: str)-> int:
	num_of_paragraph = 0
	try:
		with open(filename, "r+") as file:
			for line in file.readlines():
				file = line.split()
				num_of_paragraph += len(file)
			totalParagraph = sum(num_of_paragraph)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	finally:
		file.close()

def getTotalCharacters(text: str)-> int:
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

def getTotalCharacters(file: str)-> int:
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

def getTotalWords(text: str)-> int:
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

def getTotalWords(file: str)-> int:
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

def getTotalSentences(text: str)->int:
	pass

def getTotalCountsOfCertainCharacter(certainCharacter: str)-> int:
	pass

def getTotalCountsOfListedCharacters(listedCharacters: list[str])-> int:
	Dict = {}
	return dict.items(Dict)

def getTotalCountsOfListedWords(listedWords: list[str])-> int: 
	pass

def getAverageLengthOfWords():
	pass

def getAverageLengthOfSentences():
	pass

def getAverageNumbersOfSentencesPerParagraph():
	pass