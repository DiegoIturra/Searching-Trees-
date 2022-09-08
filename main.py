from binarySearchTree import BinarySearchTree
from AVLSearchTree import AVLSearchTree
import random

if __name__ == '__main__':
	
	#Ejemplo de instancia
	tree = AVLSearchTree()
	tree.insert(33)
	tree.insert(9)
	tree.insert(53)
	tree.insert(8)
	tree.insert(61)
	tree.insert(21)
	tree.insert(11)

	tree.show_height()