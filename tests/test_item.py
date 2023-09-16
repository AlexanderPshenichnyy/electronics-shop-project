# """Здесь надо написать тесты с использованием pytest для модуля item."""
import json
import os, pytest, csv
from src.item import Item
from src.exception import InstantiateCSVError


@pytest.fixture
def items():
	item = Item("Смартфон", 10000, 20)
	return item


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


def test_all_items(items):
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


def test_name_setter(items):
	assert items.name == 'Смартфон'
	items.name = 'СуперСмартфон'
	assert items.name == 'СуперСмарт'
	items.name = ''
	assert items.name == ''


def test_string_to_number():
	assert Item.string_to_number('5') == 5
	assert Item.string_to_number('5.0') == 5
	assert Item.string_to_number('5.5') == 5


def test_item_initialization(items):
	assert items.name == "Смартфон"
	assert items.price == 10000
	assert items.quantity == 20


def test_repr(items):
	assert repr(items) == "Item('Смартфон', 10000, 20)"


def test_str(items):
	assert str(items.name) == 'Смартфон'


def test_cut_name(items):
	items.name = 'Суперсмартфон'
	assert items.name == "Суперсмарт"


def test_raises_file_not_found():
	with pytest.raises(FileNotFoundError, match='Отсутствует файл items.csv'):
		Item.csv_path = 'items.csv'
		Item.ABSOLUTE_PATH = os.path.abspath(Item.csv_path)
		Item.instantiate_from_csv()


def test_instantiate_csv_error():
	with pytest.raises(InstantiateCSVError):
		data = [
			{'price': 100, 'quantity': 1},
			{'price': 1010, 'quantity': 12}
		]
		with open('test_data.csv', 'w', encoding='cp1251', newline='') as data_csv:
			row_names = ['price', 'quantity']
			writing_to_a_file = csv.DictWriter(data_csv, fieldnames=row_names)
			writing_to_a_file.writeheader()
			writing_to_a_file.writerows(data)
		Item.ABSOLUTE_PATH = 'test_data.csv'
		Item.instantiate_from_csv()

