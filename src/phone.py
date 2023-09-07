from src.item import Item


class Phone(Item):
	def __init__(self, name: str, price: float, quantity: int, number_of_sim):
		super().__init__(name, price, quantity)
		self._number_of_sim = number_of_sim

	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

	def __str__(self):
		return str(self.name)

	def __radd__(self, other):
		return int(self.quantity + other.quantity)

	def __add__(self, other):
		if isinstance(self, Phone):
			return int(self.quantity + other.quantity)

	@property
	def number_of_sim(self):
		return self._number_of_sim

	@number_of_sim.setter
	def number_of_sim(self, value):
		if not isinstance(value, int) or value <= 0:
			raise ValueError(': Количество физических SIM-карт должно быть целым числом больше нуля.')
		self._number_of_sim = value
