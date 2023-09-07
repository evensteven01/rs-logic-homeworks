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
				file = line.split("\n")
				num_of_paragraph += len(file)
			totalParagraph = sum(num_of_paragraph)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	finally:
		file.close()

def getTotalCharactersInText(text: str)-> int:
	num_of_characters = 0

	if text is None:
		return num_of_characters

	for line in text.split():
		num_of_characters += len(list(line))
	totalCharacters = sum(num_of_characters)
	return totalCharacters

def getTotalCharactersInFile(file: str)-> int:
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

def getTotalWordsInText(text: str)-> int:
	num_of_words = 0
	
	if text is None:
		return num_of_words

	for line in text.split():
		num_of_words += len(line)
	totalWords = sum(num_of_words)
	return totalWords

def getTotalWordsInFile(file: str)-> int:
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
	num_of_sentences = 0

	if text is None:
		return num_of_sentences

	for line in text.split():
		num_of_sentences += len(line)
	totalSentence = sum(num_of_sentences)
	return totalSentence

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