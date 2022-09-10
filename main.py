from AVLSearchTree import AVLSearchTree
import random


if __name__ == '__main__':
	
	#Ejemplo de instancia
	tree = AVLSearchTree()

	numbers = [*range(1,1000000)]
	random.shuffle(numbers)

	for number in numbers:
		tree.insert(number)

	tree.print_tree()
	
