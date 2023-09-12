# This module produces statistics about text
import ntk
import os
import json
import ast
import pickle

filename = "data.text"
filename2 = "data.json"

"""
	This function is to get the total numbers of paragraphs in text
"""
def getTotalParagraphsInText(text: str)-> int:
	num_of_paragraph = 0

	if text is None:
		return num_of_paragraph

	paragraphs = text.split("\n")

	for p in paragraphs:
		if p != "":
			num_of_paragraph += 1
	return num_of_paragraph

"""
	This function is to get the total numbers of paragraphs in file
"""
def getTotalParagraphsInFile(file: str)-> int:
	num_of_paragraph = 0
	try:
		with open(filename, "r+") as file:
			content = file.read()
		num_of_paragraph = getTotalParagraphsInText(content)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	return num_of_paragraph

"""
	This function is to get total numbers of characters in text
"""
def getTotalCharactersInText(text: str)-> int:
	num_of_characters = 0

	if text is None:
		return num_of_characters

	num_of_characters = len(text)
	return num_of_characters

"""
	This function is to get the total numbers of characters in file
"""
def getTotalCharactersInFile(file: str)-> int:
	num_of_characters = 0
	try:
		with open(filename, "r+") as file:
			content = file.read()
		num_of_characters = getTotalCharactersInText(content) 
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	return num_of_characters

"""
	This function is to get the total numbers of words in text
"""
def getTotalWordsInText(text: str)-> int:
	num_of_words = 0
	
	if text is None:
		return num_of_words

	words = text.split(" ")

	for w in words:
		if w != "":
			num_of_words += 1
	return num_of_words

"""
	This function is to get the total numbers of words in file
"""
def getTotalWordsInFile(file: str)-> int:
	num_of_words = 0
	try:
		with open(filename, "r+") as file:
			content = file.read()
		num_of_words = getTotalWordsInText(content)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	return num_of_words

"""
	This function is to get the total numbers of sentences in text
"""
def getTotalSentencesInText(text: str)-> int:
	num_of_sentences = 0

	if text is None:
		return num_of_sentences

	sentences = text.split(".")

	for s in sentences:
		if s != "":
			num_of_sentences += 1
	return num_of_sentences

"""
	This function is get the total numbers of sentences in file
"""
def getTotalSentencesInFile(file: str)-> int:
	num_of_sentences = 0
	try:
		with open(filename, "r") as file:
			content = file.read()
		num_of_sentences = getTotalSentencesInText(content)
	except FileNotFoundError as fe:
		raise fe
	else:
		msg = "The file " + filename + " does not exist."
	return num_of_sentences

"""
	This function is to get the total numbers of certain characters.
"""
def getTotalCountsOfCertainCharacter(certainCharacter: str, text: str)-> int:
	num_of_certain_characters = 0

	if certainCharacter is None or text is None:
		return num_of_certain_characters

	for cc in text:
		if cc == certainCharacter:
			num_of_certain_characters += 1
	return num_of_certain_characters

"""
	This function is to get the total numbers of listed characters.
	In this function, we are allow to reuse other functions if its necessary
"""
def getTotalCountsOfListedCharacters(listedCharacters: list[str], text: str)-> dict[str, int]:
	"""
		listedCharacters - A list of the charcters we are looking for
		Return the count of each character, in a dict format.

		Example: Find all a's and b's in a text.
		text = "This is a text. It does have a b in it, boy oh boy!"
		result = getTotalCountsOfListedCharacters(["a", "b""], text)
		{
			"a": 3,
			"b": 3
		}
	"""
	listed_character_dict = {}

	if listed_character_dict is None or text is None:
		return

	for lc in listedCharacters:
		outcome = getTotalCountsOfCertainCharacter(lc, text)
		listed_character_dict[lc] = outcome
	return listed_character_dict

"""
	This function is to get the total numbers of listed words.
	In this function, we are allow to reuse other functions if its necessary
"""
def getTotalCountsOfListedWords(listedWords: list[str], text: str)-> dict[str, int]: 
	listed_words_dict = {}

	if listedWords is None or text is None:
		return

	for lw in listedWords:
		outcome = getTotalWordsInText(lw)
		listed_words_dict[lw] = outcome
	return listed_words_dict

"""
	This function is to the average length of words
"""
def getAverageLengthOfWords(text: str)-> int:
	averageLengthOfWords = 0

	lengthOfWords = len(getTotalWordsInText(text))

	averageLengthOfWords += lengthOfWords

	return averageLengthOfWords

"""
	This function is to get the average length of sentences
"""
def getAverageLengthOfSentences(text: str)-> int:
	averageLengthOfSentences = 0

	lengthOfsentences = len(getTotalWordsInText(text))

	averageLengthOfSentences += lengthOfWords

	return averageLengthOfSentences

"""
	This function is to get the average numbers of each sentences in in each paragarphas
"""
def getAverageNumbersOfSentencesPerParagraph(text: str)-> int:
	averageNumberOfSenetncesPerParagraph = 0

	return averageNumberOfSenetncesPerParagraph