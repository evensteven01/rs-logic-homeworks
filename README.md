# General
This repo contains homeworks for Ryan.
# Text Homework 1
Build a library of different tools. Since it should be a library usable by you or others, it should return processed data, instead of printing it.

A library should be represented as a python package. A module should correspond to a python module.

## Text Library
### Text Statistics module
This module produces statistics about text.
Write functions that:
- Gives total paragraphs in a text
- Gives total paragraphs in a file
- Total characters in a text or file
- Total words in a text or file
- Total sentences in a text or file
- Total count of a certain character
- Total counts of a list of characters (case insenstive) (return as a dictionary)
- Total counts of a list of words (case insensitvie) (return as a dictionary)
- Average length of word
- Average length of sentences.
- Average numbers of sentences per paragraph.

### Text manipulation module. 
This module manipulates text.
Write functions that:
- Capitalizes the first letter of every sentence.
- Replaces a set of words with another set of words. So you'll probably take a dictionary with a mapping of the word to find, with the replacement word.

# Text Homework 2


# Testing
To run tests and code, you need to install the dependencies using pipenv.

This will install the pacakges both for production and for development.
pipenv install --dev

To activate the environment, you would run:
pipenv shell

To deactivate the environment, you can type:
exit
