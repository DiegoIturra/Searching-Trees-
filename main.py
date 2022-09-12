from AVLSearchTree import AVLSearchTree
import random


if __name__ == '__main__':
	
	#Ejemplo de instancia
	tree = BinarySearchTree()
	
	for i in range(20):
		tree.insert(i)


	tree.print_tree()

	for i in range(20):
		print(tree.search(i))
