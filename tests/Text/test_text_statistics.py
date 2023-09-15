from src.Text.text_statistics import *

def test_getTotalParagraphsInText_one_paragraph():
	# Arrange
	text = "This is a text. It has one paragraph."
	exp_ct = 1

	# Act
	act_ct = getTotalParagraphsInText(text)

	# Assert
	assert exp_ct == act_ct