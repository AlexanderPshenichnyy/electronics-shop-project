import csv
import os


class Item:
	"""
	Класс для представления товара в магазине.
	"""
	pay_rate = 1.0
	all = []
	CSV_PATH = os.path.join('../src/items.csv')			# Глобальный путь к файлу items.csv

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
		Item.all.clear()							# Очистка списка Item.all
		with open(cls.CSV_PATH, encoding="cp1251") as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				name = row["name"]
				price = int(row["price"])
				quantity = int(row["quantity"])
				item = cls(name, price, quantity)  	# Создание экземпляра класса Item
				cls.all.append(item)  				# Добавление экземпляра в список all

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
