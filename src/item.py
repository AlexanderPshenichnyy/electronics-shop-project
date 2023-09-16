import csv
import os
from src.exception import InstantiateCSVError


class Item:
	"""
	Класс для представления товара в магазине.
	"""
	# Размер скидки
	pay_rate = 1.0
	# Список экземпляров класса Item
	all = []
	# Путь к items.csv
	csv_path = 'C:/Users/Admin/Desktop/HomeWorks/electronics-shop-project/src/items.csv'
	# Глобальный путь к файлу items.csv
	ABSOLUTE_PATH = os.path.abspath(csv_path)

	def __init__(self, name: str, price: float, quantity: int) -> None:
		"""
		Создание экземпляра класса item.

		:param name: Название товара.
		:param price: Цена за единицу товара.
		:param quantity: Количество товара в магазине.
		"""
		self.__name = name
		self.price = price
		self.quantity = quantity
		super().__init__()

	def __repr__(self):
		return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

	def __str__(self):
		return self.name

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		"""
		Обрезает название до 10 символов
		"""
		self.__name = name[:10]

	@classmethod
	def instantiate_from_csv(cls):
		try:
			with open(cls.ABSOLUTE_PATH) as csvfile:
				reader = csv.DictReader(csvfile)
				# Очистка списка Item.all
				cls.all.clear()
				for row in reader:
					#  Название товара
					name = row["name"]
					#  Стоимость товара
					price = int(row["price"])
					#  Количество товара
					quantity = int(row["quantity"])
					# Создание экземпляра класса Item
					item = cls(name, price, quantity)
					# Добавление экземпляра в список all
					cls.all.append(item)

		except FileNotFoundError:
			raise FileNotFoundError('Отсутствует файл items.csv')

		except KeyError:
			raise InstantiateCSVError('Файл items.csv повреждён')

	def calculate_total_price(self) -> float:
		"""
		Рассчитывает общую стоимость конкретного товара в магазине.

		:return: Общая стоимость товара.
		"""
		return self.price * self.quantity

	def apply_discount(self) -> float:
		"""
		Применяет установленную скидку для конкретного товара.
		"""
		self.price *= self.pay_rate
		return self.price

	@staticmethod
	def string_to_number(string):
		"""
		Конвертирует строку или число с плавающей точкой в значение типа int
		"""
		return int(float(string))
