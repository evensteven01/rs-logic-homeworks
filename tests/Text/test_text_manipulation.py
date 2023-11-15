from unittest import mock
import pytest
from pytest_mock.plugin import MockerFixture

from src.Text.text_manipulation import *

@pytest.mark.parametrize(
    "text,exp_text",
    [
        (None,None),
        ("",""),
        ("\n","\n"),
        ("This is a text. It has one paragraph.","This is a text. It has one paragraph."),
        ("this is a text. it has one paragraph.\n","This is a text. It has one paragraph.\n"),
        ("is this a text? it is!","Is this a text? It is!"),
    ]
)
def test_capitalizeFirstLetterOfEverySentences(text: str, exp_text: str) -> None:
    # Arrange

    # Act
    act_text = capitalizeFirstLetterOfEverySentences(text)

    # Assert
    assert exp_text == act_text
