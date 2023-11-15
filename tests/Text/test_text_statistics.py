from unittest import mock
import pytest
from pytest_mock.plugin import MockerFixture

from src.Text.text_statistics import *

@pytest.mark.parametrize(
    "paragraph,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("This is a text. It has one paragraph.",1),
        ("This is a text. It has one paragraph.\n",1),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",2),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph.",2),
    ]
)
def test_getTotalParagraphsInText(paragraph: str, exp_count: int) -> None:
    # Arrange

    # Acts
    act_ct = getTotalParagraphsInText(paragraph)

    # Assert
    assert exp_count == act_ct

@pytest.mark.parametrize(
    "file_content,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("This is a text. It has one paragraph.",1),
        ("This is a text. It has one paragraph.\n",1),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",2),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph.",2),
    ]
)
def testgetTotalParagraphsInFile(file_content: str, exp_count: int, mocker: MockerFixture) -> None:
    # Arrange
    dummy_file = "File.txt"


    # Act
    # with mock.patch('builtins.open', mock.mock_open(read_data=file_content)) as mock_file:
    with mock.patch('src.Text.text_statistics.open', mock.mock_open(read_data=file_content)) as mock_file:
        act_ct = getTotalParagraphsInFile(dummy_file)

    # Assert
    assert exp_count == act_ct

@pytest.mark.parametrize(
    "paragraph,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",1),
        ("This is a text. It has one paragraph.",37),
        ("This is a text. It has one paragraph.\n",38),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",64),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph.",65),
    ]
)
def test_getTotalCharactersInText(paragraph: str, exp_count: int) -> None:
    # Arrange

    # Act
    act_ct = getTotalCharactersInText(paragraph)

    # Assert
    assert exp_count == act_ct


@pytest.mark.parametrize(
    "file_content,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",1),
        ("This is a text. It has one paragraph.",37),
        ("This is a text. It has one paragraph.\n",38),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",64),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph.",65),
    ]
)
def test_getTotalCharactersInFile(file_content: str, exp_count: int) -> None:
    # Arrange
    dummy_file = "File.txt"


    # Act
    # with mock.patch('builtins.open', mock.mock_open(read_data=file_content)) as mock_file:
    with mock.patch('src.Text.text_statistics.open', mock.mock_open(read_data=file_content)) as mock_file:
        act_ct = getTotalCharactersInFile(dummy_file)

    # Assert
    assert exp_count == act_ct

@pytest.mark.parametrize(
    "paragraph,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("This is a text. It has one paragraph.",8),
        ("This is a text. It has one paragraph.\n",8),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",12),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph.",12),
    ]
)
def test_getTotalWordsInText(paragraph: str, exp_count: int) -> None:
    # Arrange

    # Act
    act_ct = getTotalWordsInText(paragraph)

    # Assert
    assert exp_count == act_ct


@pytest.mark.parametrize(
    "file_content,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("This is a text. It has one paragraph.",8),
        ("This is a text. It has one paragraph.\n",8),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",12),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph.",12),
    ]
)
def test_getTotalWordsInFile(file_content: str, exp_count: int) -> None:
    # Arrange
    dummy_file = "File.txt"


    # Act
    # with mock.patch('builtins.open', mock.mock_open(read_data=file_content)) as mock_file:
    with mock.patch('src.Text.text_statistics.open', mock.mock_open(read_data=file_content)) as mock_file:
        act_ct = getTotalWordsInFile(dummy_file)

    # Assert
    assert exp_count == act_ct

@pytest.mark.parametrize(
    "paragraph,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("This is a text. It has one paragraph.",2),
        ("This is a text. It has one paragraph..\n",2),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph..",3),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",3),
    ]
)
def test_getTotalSentencesInText(paragraph: str, exp_count: int) -> None:
    # Arrange

    # Act
    act_ct = getTotalSentencesInText(paragraph)

    # Assert
    assert exp_count == act_ct


@pytest.mark.parametrize(
    "file_content,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("This is a text. It has one paragraph.",2),
        ("This is a text. It has one paragraph..\n",2),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph..",3),
        ("This is a text. It has one paragraph.\nThis is another paragraph.",3),
    ]
)
def test_getTotalSentencesInFile(file_content: str, exp_count: int) -> None:
    # Arrange
    dummy_file = "File.txt"


    # Act
    # with mock.patch('builtins.open', mock.mock_open(read_data=file_content)) as mock_file:
    with mock.patch('src.Text.text_statistics.open', mock.mock_open(read_data=file_content)) as mock_file:
        act_ct = getTotalSentencesInFile(dummy_file)

    # Assert
    assert exp_count == act_ct


@pytest.mark.parametrize(
    "paragraph,char_to_find, exp_count",
    [
        (None, None, 0),
        (None, "p", 0),
        ("", "p", 0),
        ("", None, 0),
        ("This is a text.", "z", 0),
        ("This is a text.", "h", 1),
        ("This is a text.", "i", 2),
        ("This is a text.", "t", 2),
        ("This is a text. It has one paragraph..\n\nThis is another.", "T", 2),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph..", "\n" ,2),
    ]
)
def test_getTotalCountsOfCertainCharacter(paragraph: str, char_to_find: str, exp_count: int) -> None:
    # Arrange

    # Act
    act_ct = getTotalCountsOfCertainCharacter(char_to_find, paragraph)

    # Assert
    assert exp_count == act_ct


@pytest.mark.parametrize(
    "text,chars_to_find,exp_count",
    [
        (None, ["p"], {"p": 0}),
        ("", ["p"], {"p": 0}),
        ("", None, {}),
        ("This is a text.", ["z"], {"z": 0}),
        ("This is a text.", ["h"], {"h": 1}),
        ("This is a text.", ["i", "z"], {"i": 2, "z": 0}),
        ("This is a text.", ["t"], {"t": 2}),
        ("This is a text. It has one paragraph..\n\nThis is another.", ["T"], {"T": 2}),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph..", ["\n"], {"\n": 2}),
    ]
)
def test_getTotalCountsOfListedCharacters(text: str, chars_to_find: list[str], exp_count: int) -> None:
    # Arrange

    # Act
    act_ct = getTotalCountsOfListedCharacters(chars_to_find, text)

    # Assert
    assert exp_count == act_ct

@pytest.mark.parametrize(
    "text,words_to_find,exp_count",
    [
        (None, ["this"], {"this": 0}),
        ("", ["this"], {"this": 0}),
        ("", None, {}),
        ("This is a text.", ["This"], {"This": 1}),
        ("This is a text.", ["you"], {"you": 0}),
        ("This is a cool text from me.", ["from", "cool"], {"from": 1, "cool": 1}),
        ("This is a text. The text is this", ["text"], {"text": 2}),
        ("This is a text. It has one paragraph..\n\nThis is another.", ["This"], {"This": 2}),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph..", ["paragraph"], {"paragraph": 2}),
    ]
)
def test_getTotalCountsOfListedWords(text: str, words_to_find: list[str], exp_count: int):
    # Arrange

    # Act
    act_ct = getTotalCountsOfListedWords(words_to_find, text)

    # Assert
    assert exp_count == act_ct

@pytest.mark.parametrize(
    "text,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("Hi.",2),
        ("This is a text. It has one paragraph.",3.5),
        ("This is a text. It has one paragraph..\n",3.5),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph..",4.167),
    ]
)
def test_getAverageLengthOfWords(text: str, exp_count: float) -> None:
    # Arrange

    # Act
    act_ct = getAverageLengthOfWords(text)

    # Assert
    assert pytest.approx(exp_count, .1) == act_ct

@pytest.mark.parametrize(
    "text,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("Hi.",1),
        ("This is a text. It has one paragraph.",4),
        ("This is a text. It has one paragraph..\n",4),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph that is longer..",4.667),
    ]
)
def test_getAverageLengthOfSentences(text: str, exp_count: float) -> None:
    # Arrange

    # Act
    act_ct = getAverageLengthOfSentences(text)

    # Assert
    assert pytest.approx(exp_count, .1) == act_ct

@pytest.mark.parametrize(
    "text,exp_count",
    [
        (None,0),
        ("",0),
        ("\n",0),
        ("Hi.",1),
        ("This is a text. It has one paragraph.",2),
        ("This is a text. It has one paragraph..\n",2),
        ("This is a text. It has one paragraph.\n\nThis is another paragraph that is longer..",1.5),
    ]
)
def test_getAverageNumbersOfSentencesPerParagraph(text: str, exp_count: float) -> None:
    # Arrange

    # Act
    act_ct = getAverageNumbersOfSentencesPerParagraph(text)

    # Assert
    assert pytest.approx(exp_count, .1) == act_ct
