# """Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.mark.parametrize('name, price, quantity, expected', [
	("Смартфон", 10000, 20, 200000),
	("Ноутбук", 20000, 5, 100000)
]
						)
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
	assert item1, item2 == ['<src.item.Item object at 0x000002932B8E88D0>',
							'<src.item.Item object at 0x000002932B929450>']
