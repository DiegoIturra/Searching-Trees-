from abc import ABC, abstractmethod

class BinaryTreeClass(ABC):

	@abstractmethod
	def insert(self,value):
		pass

	@abstractmethod
	def search(self,value):
		pass



