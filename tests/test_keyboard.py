import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
	kb1 = Keyboard('Dark Project KD87A', 9600, 5)
	return kb1


def test_keyboard_language(keyboard):
	assert keyboard.language == 'EN'


def test_change_lang(keyboard):
	keyboard.__language = 'EN'
	keyboard.change_lang()
	assert keyboard.language == 'RU'
