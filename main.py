from AVLSearchTree import AVLSearchTree
from binarySearchTree import BinarySearchTree
import random


if __name__ == '__main__':
	
	#Ejemplo de instancia
	"""tree = BinarySearchTree()
	
	for i in range(20):
		tree.insert(i)


	tree.print_tree()

	for i in range(20):
		print(tree.search(i))
	"""

	tree = BinarySearchTree()
	
	for i in range(10000):
		tree.insert(i)


	tree.print_tree()

	for i in range(10):
		print(tree.search(i))
	



	#print(tree.__class__.__name__)
	


