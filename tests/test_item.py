# """Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.mark.parametrize('name, price, quantity, expected', [
	("Смартфон", 10000, 20, 200000),
	("Ноутбук", 20000, 5, 100000)
])
def test_calculate_total_price(name, price, quantity, expected):
	items = Item(name, price, quantity)
	assert items.calculate_total_price() == expected


@pytest.mark.parametrize('name, price, quantity, expected', [
	("Смартфон", 10000, 20, 8000.0)
])
def test_apply_discount(name, price, quantity, expected):
	item1 = Item(name, price, quantity)
	Item.pay_rate = 0.8
	assert item1.apply_discount() == expected


def test_all_items():
	item1 = Item("Смартфон", 10000, 20)
	item2 = Item("Ноутбук", 20000, 5)
	assert item1, item2 == [
		'<src.item.Item object at 0x000002932B8E88D0>',
		'<src.item.Item object at 0x000002932B929450>'
	]


def test_instantiate_from_csv():
	Item.all = []
	Item.instantiate_from_csv()
	assert len(Item.all) == 5
	assert Item.all[0].name == 'Смартфон'


def test_name_setter():
	item = Item("Смартфон", 10000, 20)
	assert item.name == 'Смартфон'
	item.name = 'СуперСмартфон'
	assert item.name == 'СуперСмарт'
	item.name = ''
	assert item.name == ''


def test_string_to_number():
	assert Item.string_to_number('5') == 5
	assert Item.string_to_number('5.0') == 5
	assert Item.string_to_number('5.5') == 5


def test_repr():
	item = Item("Смартфон", 10000, 20)
	assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str():
	item = Item("Смартфон", 10000, 20)
	assert str(item) == 'Смартфон'
