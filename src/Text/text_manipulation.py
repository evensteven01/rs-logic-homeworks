# This module will manipulates text
from text_statistics import *
import re

"""
This function is to capitalizes every first letters in every sentences
"""
def capitalizeFirstLetterOfEverySentences(text: str)-> str:
	firstLetter = ""
	num_of_sentences = 0

	sentences = text.split(".")

	for s in sentences:
		firstLetter = s.capitalize()

		num_of_sentences += getTotalSentencesInText(firstLetter)

	return firstLetter

"""
	This function is to replece set of words with other set of words
"""
def replacementSetOfWords(listedWords: list[str], text: str)-> dict[str, str]:
	replaceWords = ""

	word_list = getTotalCountsOfListedWords(text)

	return replaceWords