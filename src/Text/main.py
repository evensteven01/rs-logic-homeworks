from text_statistics import *
from text_manipulation import capitalizeFirstLetterOfEverySentences, replacementSetOfWords

if __name__ == '__main__':

	userInput = input("Please enter your text:_")
	userWord = input("Please enter a word to be replace:_")
	new_word = input("What do you want ot replace with?:_")
	userCharacter = (input("Please enter a character:_"))
	userlistedCharacter = list(input("Please enter a list of characters:_"))
	userlistedWords = list(input("Please enter a list of words:_"))
	"""
		text statistics functions calls
	"""
	print(getTotalParagraphsInText(userInput))
	print(getTotalCharactersInText(userInput))
	print(getTotalWordsInText(userInput))
	print(getTotalSentencesInText(userInput))
	print(getTotalCountsOfCertainCharacter(userCharacter,userInput))
	print(getTotalCountsOfListedCharacters(userlistedCharacter,userInput))
	print(getTotalCountsOfListedWords(userlistedWords, userInput))
	print(getAverageLengthOfWords(userInput))
	print(getAverageLengthOfSentences(userInput))
	print(getAverageNumbersOfSentencesPerParagraph(userInput))

	"""
		text manipuation functions calls
	"""
	print(capitalizeFirstLetterOfEverySentences(userInput))
	print(replacementSetOfWords({userWord: new_word}, userInput))