 # This module produces statistics about text
import os

def getTotalParagraphsInText(text: str)-> int:
    """
        This function is to get the total numbers of paragraphs in text
    """
    num_of_paragraph = 0

    if text is None:
        return num_of_paragraph

    paragraphs = text.split("\n")

    for p in paragraphs:
        if p != "":
            num_of_paragraph += 1
    return num_of_paragraph


def getTotalParagraphsInFile(fileName: str)-> int:
    """
        This function is to get the total numbers of paragraphs in file
    """
    num_of_paragraph = 0
    try:
        with open(fileName, "r+") as file:
            content = file.read()
        num_of_paragraph = getTotalParagraphsInText(content)
    except FileNotFoundError as fe:
        raise fe
    else:
        msg = "The file " + fileName + " does not exist."
    return num_of_paragraph


def getTotalCharactersInText(text: str)-> int:
    """
        This function is to get total numbers of characters in text
    """
    num_of_characters = 0

    if text is None:
        return num_of_characters

    num_of_characters = len(text)
    return num_of_characters


def getTotalCharactersInFile(fileName: str)-> int:
    """
        This function is to get the total numbers of characters in file
    """
    num_of_characters = 0
    try:
        with open(fileName, "r+") as file:
            content = file.read()
        num_of_characters = getTotalCharactersInText(content) 
    except FileNotFoundError as fe:
        raise fe
    else:
        msg = "The file " + fileName + " does not exist."
    return num_of_characters


def getTotalWordsInText(text: str)-> int:
    """
        This function is to get the total numbers of words in text
    """
    num_of_words = 0
    
    if text is None:
        return num_of_words

    words = text.split()

    for word in words:
        if word != "":
            num_of_words += 1
    return num_of_words


def getTotalWordsInFile(fileName: str)-> int:
    """
        This function is to get the total numbers of words in file
    """
    num_of_words = 0
    try:
        with open(fileName, "r+") as file:
            content = file.read()
        num_of_words = getTotalWordsInText(content)
    except FileNotFoundError as fe:
        raise fe
    else:
        msg = "The file " + fileName + " does not exist."
    return num_of_words


def getTotalSentencesInText(text: str)-> int:
    """
        This function is to get the total numbers of sentences in text
    """
    num_of_sentences = 0

    if text is None:
        return num_of_sentences

    sentences = text.split(".")

    for sentence in sentences:
        if sentence.strip() != "":
            num_of_sentences += 1
    return num_of_sentences


def getTotalSentencesInFile(fileName: str)-> int:
    """
        This function is get the total numbers of sentences in file
    """
    try:
        with open(fileName, "r+") as file:
            content = file.read()
        num_of_sentences = getTotalSentencesInText(content)
    except FileNotFoundError as fe:
        raise fe
    else:
        msg = "The file " + fileName + " does not exist."
    return num_of_sentences


def getTotalCountsOfCertainCharacter(certainCharacter: str, text: str)-> int:
    """
        This function is to get the total numbers of certain characters.
    """
    num_of_certain_characters = 0

    if certainCharacter is None or text is None:
        return num_of_certain_characters

    for cc in text:
        if cc == certainCharacter:
            num_of_certain_characters += 1
    return num_of_certain_characters


def getTotalCountsOfListedCharacters(listedCharacterList: list[str], text: str)-> dict[str, int]:
    """
        This function is to get the total numbers of listed characters.
        In this function, we are allow to reuse other functions if its necessary
    """

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
    listedCharacterDict = {}

    if listedCharacterList is None:
        return listedCharacterDict

    if text is None:
        return {ch: 0 for ch in listedCharacterList}

    for listedCharacter in listedCharacterList:
        if listedCharacter != "":
            outcome = getTotalCountsOfCertainCharacter(listedCharacter, text)
            listedCharacterDict[listedCharacter] = outcome
    return listedCharacterDict


def getTotalCountsOfListedWords(listedWords: list[str], text: str)-> dict[str, int]:
    """
        This function is to get the total numbers of listed words.
        In this function, we are allow to reuse other functions if its necessary
    """ 
    listedWordsDict = {}

    if listedWords is None:
        return listedWordsDict

    if text is None:
        return {w: 0 for w in listedWords}

    words = text.split()

    for lenWord in listedWords:
        outcome = 0
        for word in words:
            word = word.strip('.?,!')
            if word == lenWord:
                outcome += 1
        listedWordsDict[lenWord] = outcome
    return listedWordsDict


def getAverageLengthOfWords(text: str)-> int:
    """
        This function is to the average length of words
    """
    averageLengthOfWords = 0
    lengthOfWords = 0

    if text is None:
        return averageLengthOfWords

    words = [w.strip('.?,!') for w in text.split()]

    for word in words:
        lengthOfWords += len(word)

        if lengthOfWords == 0:
            averageLengthOfWords = 0
        else:
            averageLengthOfWords = (lengthOfWords / getTotalWordsInText(text))

    return averageLengthOfWords


def getAverageLengthOfSentences(text: str)-> int:
    """
        This function is to get the average length of sentences
    """
    averageLengthOfSentences = 0
    totalWords = 0

    if text is None:
        return averageLengthOfSentences

    sentences = text.split(".")

    for sentence in sentences:
        if sentence == "":
            continue

        numOfWordsInSentence = getTotalWordsInText(sentence)

        totalWords += numOfWordsInSentence

        if totalWords == 0:
            totalWords = 0
        else:
            averageLengthOfSentences = (totalWords / getTotalSentencesInText(text))           

    return averageLengthOfSentences

def getAverageNumbersOfSentencesPerParagraph(text: str)-> int:
    """
        This function is to get the average numbers of each sentences in in each paragarphas
    """
    averageNumberOfSentencesPerParagraph = 0
    totalSentences = 0

    if text is None:
        return averageNumberOfSentencesPerParagraph

    paragraphs = text.split("\n")

    for paragraph in paragraphs:
        if paragraph == "":
            continue

        sentencesPerParagraph = getTotalSentencesInText(paragraph)

        totalSentences += sentencesPerParagraph

        if totalSentences == 0:
            totalSentences = 0
        else:
            averageNumberOfSentencesPerParagraph = (totalSentences / getTotalParagraphsInText(text))

    return averageNumberOfSentencesPerParagraph