from AVLSearchTree import AVLSearchTree


if __name__ == '__main__':
	
	#Ejemplo de instancia
	tree = AVLSearchTree()

	for i in range(20):
		tree.insert(i+1)

	tree.print_tree()
	
