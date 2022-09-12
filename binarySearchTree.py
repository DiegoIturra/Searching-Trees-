from binaryTreeClass import BinaryTreeClass , Node

class BinarySearchTree(BinaryTreeClass):

	def __init__(self, root):
		super().__init__(root)

	def __inorder(self,root):
		if root is not None:
			self.__inorder(root.left)
			print(root.value)
			self.__inorder(root.right)

	def __create_node(self,value):
		return Node(value)

	def __insert_node(self,root,value):
		if not root:
			root = self.__create_node(value)
		else:
			new_node = self.__create_node(value)

			# insertar a la izquierda
			if value < root.value:
				root.left = self.__insert_node(root.left,value)
			# insertar a la derecha
			else:
				root.right = self.__insert_node(root.right,value)

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


	# metodos publicos
	def print_tree(self):
		self.__inorder(self.root)

	def insert(self,value):
		self.root = self.__insert_node(self.root,value)

	def search(self,value):
		node = self.__create_node(value)
		return self.__exist(self.root,node)
