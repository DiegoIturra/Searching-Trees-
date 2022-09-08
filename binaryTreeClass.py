from abc import ABC, abstractmethod

class Node:

	def __init__(self,value):
		self.value = value
		self._left = None
		self._right = None

		self._height = 1
		self._balance_factor = 0

	@property
	def left(self):
		return self._left

	@left.setter
	def left(self,value):
		self._left = value

	@property
	def right(self):
		return self._right

	@right.setter
	def right(self,value):
		self._right = value

	@property
	def balance_factor(self):
		return self._balance_factor

	@balance_factor.setter
	def balance_factor(self,balance_factor):
		self._balance_factor = balance_factor

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,height):
		self._height = height


	def __eq__(self,other):
		if isinstance(other,Node):
			return self.value == other.value
		return False


	def __lt__(self,other):
		if isinstance(other,Node):
			return self.value < other.value
		return False


	def __gt__(self,other):
		if isinstance(other,Node):
			return self.value > other.value
		return False


	def __str__(self):
		return f"Node: {self.value}"


class BinaryTreeClass(ABC):

	@abstractmethod
	def insert(self,value):
		pass

	@abstractmethod
	def search(self,value):
		pass
