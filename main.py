from tracemalloc import start
from AVLSearchTree import AVLSearchTree
from binarySearchTree import BinarySearchTree
import random

from redBlackTree import RedBlackTree

from time import time


if __name__ == '__main__':
	
	#Ejemplo de instancia
	"""tree = BinarySearchTree()
	
	for i in range(20):
		tree.insert(i)


	tree.print_tree()

	for i in range(20):
		print(tree.search(i))
	"""

	tree = RedBlackTree()

	n = 100000

	start_time = time()

	for i in range(n):
		tree.insert(random.randint(0,100000))

	print("Tiempo de insercion promedio: ",(time() - start_time)/100," ms")


	# tree.print_tree()

	start_time = time()

	for i in range(n):
		tree.search(random.randint(0,100000))

	print("Tiempo de busqueda promedio: ",(time() - start_time)/100," ms")
	



	#print(tree.__class__.__name__)
	


