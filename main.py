from AVLSearchTree import AVLSearchTree


if __name__ == '__main__':
	
	#Ejemplo de instancia
	tree = AVLSearchTree()

	tree.insert(30)
	tree.insert(20)
	tree.insert(10)

	tree.print_tree()
	tree.balancear()

	print()
	print()

	tree.print_tree()

	print(tree.search(10))
	print(tree.search(20))
	print(tree.search(30))
	
