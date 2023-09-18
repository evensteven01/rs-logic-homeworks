# This module will manipulates text
from text_statistics import *
import re

"""
This function is to capitalizes every first letters in every sentences
"""
def capitalizeFirstLetterOfEverySentences(text: str)-> str:
	capitalizedSentence = ""

	capitalizedSentenceList = []

	sentences = text.split(".")

	for s in sentences:
		capitalizedSentence = s.capitalize()
		capitalizedSentenceList.append(capitalizedSentence)

	cs = ".".join(capitalizedSentenceList)

	return cs

"""
	This function is to replece set of words with other set of words
"""
def replacementSetOfWords(wordReplacement: dict[str, str], text: str)-> str:
	replaceWords = ""

	words = text.split(" ")

	for rw in words:
		# check if this word should be replace?
		if :
			pass

		# replace old word with new word
		text.replace()

	return 