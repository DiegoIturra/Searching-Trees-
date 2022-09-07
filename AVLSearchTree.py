from binaryTreeClass import Node,BinaryTreeClass

class AVLSearchTree(BinaryTreeClass):

	def __init__(self):
		self.root = None


	def __inorder(self,root):
		if root is not None:
			self.__inorder(root.left)
			print(root)
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





