from tracemalloc import start
from AVLSearchTree import AVLSearchTree
from binarySearchTree import BinarySearchTree
import random

from redBlackTree import RedBlackTree

from time import time


if __name__ == '__main__':

	tree = BinarySearchTree()

	n = 100000

	values = []

	for i in range(n):
		values.append(random.randint(0, n))


	start_time = time()
	for i in range(n):
		tree.insert(values[i])

	print(f"Tiempo de insercion total {n} elementos desordenados: {(time() - start_time)} s")

	
	tree = BinarySearchTree()
	values.sort()

	start_time = time()
	for i in range(n):
		print(f"{i}: {values[i]}")
		tree.insert(values[i])
	print(f"Tiempo de insercion total {n} elementos ordenados: {(time() - start_time)} s")




