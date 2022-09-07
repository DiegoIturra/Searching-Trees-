from binarySearchTree import BinarySearchTree
from AVLSearchTree import AVLSearchTree
import random

if __name__ == '__main__':
	
	#Ejemplo de instancia
	tree = AVLSearchTree()
	tree.insert(69)
	tree.insert(40)
	tree.insert(100)
	tree.insert(150)
	tree.insert(80)
	tree.insert(60)
	tree.insert(30)

	tree.print_tree()

	print(tree.search(40))
	print(tree.search(1000))
	print(tree.search(30))
	print(tree.search(150))
	print(tree.search(79))
	print(tree.search(89))