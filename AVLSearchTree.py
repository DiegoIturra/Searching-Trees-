from binaryTreeClass import Node,BinaryTreeClass

class AVLSearchTree(BinaryTreeClass):

	def __init__(self):
		self.root = None

	#Calcula la altura de un nodo a partir del maximo entre el sub arbol
	#izquiero y sub arbol derecho
	def __calculate_height(self,node):
		if node is None:
			return 0
		return 1 + max(self.__get_height(node.left) , self.__get_height(node.right))


	#Retorna el valor de la alura asociado al nodo pasado
	def __get_height(self,node):
		if node is not None:
			return node.height
		return 0

	#Retorn el factor de balance de un nodo especifico
	def __get_balance_factor(self,node):
		if not node:
			return 0
		return self.__get_height(node.left) - self.__get_height(node.right)


	#Balancear un nodo especifico
	def __balance(self,node):
		pass


	def __inorder(self,root):
		if root is not None:
			self.__inorder(root.left)
			print(f"{root} / heigth : {root.height} / balance_factor : {root.balance_factor}")
			self.__inorder(root.right)



	def __create_node(self,value):
		return Node(value)

		

	def __insert_node(self,root,value):
		if not root:
			return self.__create_node(value)
		else:
			new_node = self.__create_node(value)
			#insertar a la izquierda
			if new_node < root:
				root.left = self.__insert_node(root.left,value)
			#insertar a la derecha
			elif new_node > root:
				root.right = self.__insert_node(root.right,value)
		
		root.height = self.__calculate_height(root)
		root.balance_factor = self.__get_balance_factor(root)
		return root


	def __exist(self,root,node):
		if not root:
			return False
		if root == node:
			return True
		if node < root:
			return self.__exist(root.left,node)
		else:
			return self.__exist(root.right,node)



	def print_tree(self):
		self.__inorder(self.root)


	def insert(self,value):
		self.root = self.__insert_node(self.root,value)


	def search(self,value):
		node = self.__create_node(value)
		return self.__exist(self.root,node)

	#Metodos de prueba (Eliminar despues)
	def show_height(self):
		self.__inorder(self.root)





