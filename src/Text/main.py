from text_statistics import *
from text_manipulation import capitalizeFirstLetterOfEverySentences, replacementSetOfWords

if __name__ == '__main__':
	automate = input("Do you want to input(i), or hardcode(h)?")

	if automate.lower() == "h":
		userInput = "This is a sentence. And this is another. \nNow we have a new paragraph. Dogs are not red.\n\nGoodbye."
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
		text statistics functions calls
	"""
	print("The total paragraphs are", getTotalParagraphsInText(userInput))
	print("The total characters are", getTotalCharactersInText(userInput))
	print("The total words are", getTotalWordsInText(userInput))
	print("The total sentences are", getTotalSentencesInText(userInput))
	print("The total counts of certain characters are", getTotalCountsOfCertainCharacter(userCharacter,userInput))
	print("The total counts of listed characters are", getTotalCountsOfListedCharacters(userlistedCharacter,userInput))
	print("The total counts of listed words are", getTotalCountsOfListedWords(userlistedWords, userInput))
	print("The average length of words is", getAverageLengthOfWords(userInput))
	print("The average length of sentences are", getAverageLengthOfSentences(userInput)) #x
	print("The average numbers of sentences per paragraph are", getAverageNumbersOfSentencesPerParagraph(userInput)) #x

	"""
		text manipulation functions calls
	"""
	print("The capitalized sentences are", capitalizeFirstLetterOfEverySentences(userInput)) #x
	print("The old word is replaced by", replacementSetOfWords({userWord: newWord}, userInput))