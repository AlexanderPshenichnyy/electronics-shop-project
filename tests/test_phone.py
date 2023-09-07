import pytest

from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone_quantity():
	"""Создание экземпляра класса"""
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	return phone1


@pytest.fixture
def item_quantity():
	"""Создание экземпляра"""
	item1 = Item("Смартфон", 10000, 20)
	return item1


def test_add_quantity(phone_quantity, item_quantity):
	assert phone_quantity + item_quantity == 25


def test_radd_quantity(item_quantity, phone_quantity):
	assert item_quantity + phone_quantity == 25


def test_isinstance():
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	phone1._number_of_sim = 0
	assert 'ValueError: : Количество физических SIM-карт должно быть целым числом больше нуля.'


def test_repr():
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
	phone1 = Phone("iPhone 14", 120_000, 5, 2)
	assert str(phone1) == 'iPhone 14'
