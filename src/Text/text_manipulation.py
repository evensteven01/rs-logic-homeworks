# This module will manipulates text
from src.Text.text_statistics import *

def capitalizeFirstLetterOfEverySentences(text: str)-> str:
	"""
		This function is to capitalizes every first letters in every sentences
	"""
	capitalizedSentenceList = []

	if text is None:
		return None

	if text.strip() == "?,!":
		return text

	sentences = text.split(".")

	# It appears that every first letter are capitaized in every word rather every sentences
	# It need to use index in order to get every first letter of each sentences to be capitaized
	for sentence in sentences:
		sentence = sentence.strip()
		print(f"Before capitalize: {sentence}")
		capitalizedSentence = sentence.capitalize()
		print(f"After capitalize: {capitalizedSentence}")
		capitalizedSentenceList.append(capitalizedSentence)

	cs = ". ".join(capitalizedSentenceList).strip()

	return cs

def replacementSetOfWords(wordReplacement: dict[str, str], text: str)-> str:
	"""
		This function is to replece set of words with other set of words
	"""
	new_word_list = [] # Create a new empty dictionary to store the modified words

	words = text.split() # split the given string into list of words

	for rw in words: # Loop through each word in the list of words
		# check if this word should be replace?
		if rw in wordReplacement.keys(): # check if the current word is equal to wordReplacement's keys
			new_word_list.append(wordReplacement[rw]) # If the word is equal to wordReplacement's keys, t
			# then append it to new dictionary
		else:
			new_word_list.append(rw) # If the word is not equal to wordReplacement's keys, then append it new dictionary
	modified_str = " ".join(new_word_list) # join the new list of words into a string with spaces between each word
	return modified_str # Return the modified string