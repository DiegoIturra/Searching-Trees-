from tracemalloc import start
from AVLSearchTree import AVLSearchTree
from binarySearchTree import BinarySearchTree
import random
import sys

from redBlackTree import RedBlackTree

from time import time


if __name__ == '__main__':

	bst = BinarySearchTree()
	avl = AVLSearchTree()
	rbt = RedBlackTree()

	# Tamaño de arreglo de entrada
	n = sys.argv[1]

	#str to int
	n = int(n)


	# inicializando tiempo de insercion
	bst_time = 0
	avl_time = 0
	rbt_time = 0

	# inicializando tiempo de busqueda
	bst_max_search_time = 0
	bst_random_search_time = 0
	avl_max_search_time = 0
	avl_random_search_time = 0
	rbt_max_search_time = 0
	rbt_random_search_time = 0

	for i in range(30):
		# arreglo con valores de entrada ordenados
		values = []
		for i in range(n):
			values.append(random.randint(0, n*10))
		values.sort()

		# insertar en BST
		start_time = time()
		for i in range(n):
			bst.insert(values[i])
		bst_time += (time() - start_time)*1000

		# insertar en AVL
		start_time = time()
		for i in range(n):
			avl.insert(values[i])
		avl_time += (time() - start_time)*1000

		# insertar en RBT
		start_time = time()
		for i in range(n):
			rbt.insert(values[i])
		rbt_time += (time() - start_time)*1000

		# elementos a buscar
		max_search = random.randint(0, 1000)+(n*10)
		random_search = values[random.randint(0, n-1)]

		# buscar en BST
		start_time = time()
		bst.search(max_search)
		bst_max_search_time += (time() - start_time)*1000
		bst.search(random_search)
		bst_random_search_time += (time() - start_time)*1000

		# buscar en AVL
		start_time = time()
		avl.search(max_search)
		avl_max_search_time += (time() - start_time)*1000
		avl.search(random_search)
		avl_random_search_time += (time() - start_time)*1000

		# buscar en RBT
		start_time = time()
		rbt.search(max_search)
		rbt_max_search_time += (time() - start_time)*1000
		rbt.search(random_search)
		rbt_random_search_time += (time() - start_time)*1000
		

	# promedio de tiempo de insercion
	bst_time /= 30
	avl_time /= 30
	rbt_time /= 30

	# promedio de tiempo de busqueda
	bst_max_search_time /= 30
	bst_random_search_time /= 30
	avl_max_search_time /= 30
	avl_random_search_time /= 30
	rbt_max_search_time /= 30
	rbt_random_search_time /= 30

	print(f"{n}, {bst_time}, {avl_time}, {rbt_time}, {bst_max_search_time}, {avl_max_search_time}, {rbt_max_search_time}, {bst_random_search_time}, {avl_random_search_time}, {rbt_random_search_time}")