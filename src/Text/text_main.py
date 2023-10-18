from src.Text.text_statistics import *
from src.Text.text_manipulation import capitalizeFirstLetterOfEverySentences, replacementSetOfWords

fileName = "src/Text/dummyData.txt"

def main():
	automate = input("Do you want to input(i), or hardcode(h)?:_")

	if automate.lower() == "h":
		userInput = "this is a sentence. And this is another. \nNow we have a new paragraph. dogs are not red.\n\nGoodbye."
		userWord = "is"
		newWord = "be"
		userCharacter = "i"
		userlistedCharacter = ["a", "t", "i"]
		userlistedWords = ["is", "red"]
	else:
		userInput = input("Please enter your text:_")
		userWord = input("Please enter a word to be replace:_")
		newWord = input("What do you want ot replace with?:_")
		userCharacter = (input("Please enter a character:_"))
		userlistedCharacter = list(input("Please enter a list of characters:_"))
		userlistedWords = list(input("Please enter a list of words:_"))
	"""
		text statistics functions calls for text
	"""
	print("The total paragraphs are", getTotalParagraphsInText(userInput), "\n")
	print("The total characters are", getTotalCharactersInText(userInput), "\n")
	print("The total words are", getTotalWordsInText(userInput), "\n")
	print("The total sentences are", getTotalSentencesInText(userInput), "\n")
	print("The total counts of certain characters are", getTotalCountsOfCertainCharacter(userCharacter,userInput), "\n")
	print("The total counts of listed characters are", getTotalCountsOfListedCharacters(userlistedCharacter,userInput), "\n")
	print("The total counts of listed words are", getTotalCountsOfListedWords(userlistedWords, userInput), "\n")
	print("The average length of words is", getAverageLengthOfWords(userInput), "\n")
	print("The average length of sentences are", getAverageLengthOfSentences(userInput), "\n")
	print("The average numbers of sentences per paragraph are", getAverageNumbersOfSentencesPerParagraph(userInput), "\n") 

	"""
		text manipulation functions calls
	"""
	print("New string after using capitalize(): ", capitalizeFirstLetterOfEverySentences(userInput), "\n")
	print("The old word is replaced by: ", replacementSetOfWords({userWord: newWord}, userInput), "\n")

	"""
		text statistics functions calls for files
	"""
	print("The total paragraphs in the file are", getTotalParagraphsInFile(fileName), "\n")
	print("The total characters in the file are", getTotalCharactersInFile(fileName), "\n")
	print("The total words in the file are", getTotalWordsInFile(fileName), "\n")
	print("The total sentences in the file are", getTotalSentencesInFile(fileName), "\n")