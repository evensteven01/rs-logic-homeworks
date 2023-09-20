# This module will manipulates text
from text_statistics import *

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
	new_word_list = [] # Create a new empty dictionary to store the modified words

	words = text.split(" ") # split the given string into list of words

	for rw in words: # Loop through each word in the list of words
		# check if this word should be replace?
		if rw in wordReplacement.keys(): # check if the current word is equal to the 
			# replace old word with new word
			new_word_list.append(wordReplacement[rw]) # If the word is equal to , append it to new dictionary
		else:
			new_word_list.append(rw) # If the word is not equal to , append the 
	modified_str = " ".join(new_word_list) # join the new list of words into a string with spaces between each word
	return modified_str # Return the modified string