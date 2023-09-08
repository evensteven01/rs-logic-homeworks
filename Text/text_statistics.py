# This module produces statistics about text
import ntk
import os
import json
import ast
import pickle
import re
from parse import parse

filename = "data.text"
filename2 = "data.json"

# this function will gets the total of paragraph
def getTotalParagraphsInText(text: str)-> int:
	num_of_paragraph = 0

	if text is None:
		return num_of_paragraph

	paragraphs = text.split("\n")

	for p in paragraphs:
		if p != "":
			num_of_paragraph += 1
	return num_of_paragraph

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

def getTotalCharactersInText(text: str)-> int:
	num_of_characters = 0

	if text is None:
		return num_of_characters

	num_of_characters = len(text)
	return num_of_characters

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

def getTotalWordsInText(text: str)-> int:
	num_of_words = 0
	
	if text is None:
		return num_of_words

	words = text.split(" ")

	for w in words:
		if w != "":
			num_of_words += 1
	return num_of_words

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

def getTotalSentencesInText(text: str)-> int:
	num_of_sentences = 0

	if text is None:
		return num_of_sentences

	sentences = text.split(".")

	for s in sentences:
		if s != "":
			num_of_sentences += 1
	return num_of_sentences

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

def getTotalCountsOfCertainCharacter(certainCharacter: str, text: str)-> int:
	num_of_certain_characters = 0

	if certainCharacter is None and text is None:
		return num_of_certain_characters
		

def getTotalCountsOfListedCharacters(listedCharacters: list[str])-> int:
	Dict = {}
	return dict.items(Dict)

def getTotalCountsOfListedWords(listedWords: list[str])-> int: 
	pass

def getAverageLengthOfWords()-> int:
	pass

def getAverageLengthOfSentences()-> int:
	pass

def getAverageNumbersOfSentencesPerParagraph()-> int:
	pass