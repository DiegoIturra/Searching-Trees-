from abc import ABC, abstractmethod

class Node:

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

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


class BinaryTreeClass(ABC):

	@abstractmethod
	def insert(self,value):
		pass

	@abstractmethod
	def search(self,value):
		pass
