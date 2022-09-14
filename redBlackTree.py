from hashlib import new
from traceback import print_tb
from turtle import right
from binaryTreeClass import RBNode, BinaryTreeClass
from binarySearchTree import BinarySearchTree


# class RedBlackTree(BinarySearchTree):

# 	def __init__(self):
# 		self.root = None

# 	def insert(self,value):
# 		pass

# 	def search(self,value):
# 		pass


class RedBlackTree(BinarySearchTree):

	def __init__(self):
		super().__init__()

	def __inorder(self,root):
		if root is not None:
			self.__inorder(root.left)
			print(root)
			self.__inorder(root.right)

	def __spray_black_node(self,node):
		if node.left is not None:
			node.left.colour = RBNode.BLACK
		if node.right is not None:
			node.right.colour = RBNode.BLACK
		
		node.colour = RBNode.RED
		if node == self.root:
			node.colour = RBNode.BLACK

	def __get_colour_balance_factor(self,node):
		left_colour_balance = 0
		right_colour_balance = 0
		if node.left is not None:
			left_colour_balance += node.left.colour
			if node.left.left is not None and node.left.left.colour == RBNode.RED:
				left_colour_balance += node.left.left.colour
			elif node.left.right is not None and node.left.right.colour == RBNode.RED:
				left_colour_balance += node.left.right.colour

		if node.right is not None:
			right_colour_balance += node.right.colour
			if node.right.left is not None and node.right.left.colour == RBNode.RED:
				right_colour_balance += node.right.left.colour
			elif node.right.right is not None and node.right.right.colour == RBNode.RED:
				right_colour_balance += node.right.right.colour
		

		if left_colour_balance == 2:
			return "left"
		elif right_colour_balance == 2:
			return "right"
		return "none"

	def __swap_colours(self,node1,node2):
		node1.colour,node2.colour = node2.colour,node1.colour

	# Rotacion izquierda
	def __left_rotation(self, node):
		aux_node = node.right
		node.right = aux_node.left
		aux_node.left = node

		self.__swap_colours(node,aux_node)

		# self.__update_height(node)
		# self.__update_height(aux_node)

		return aux_node

	# Rotacion derecha
	def __right_rotation(self, node):
		aux_node = node.left
		node.left = aux_node.right
		aux_node.right = node

		self.__swap_colours(node,aux_node)

		# self.__update_height(node)
		# self.__update_height(aux_node)

		return aux_node

	def __balance_colour(self,node):

		# verifica si el nodo tiene 2 hijos rojos consecutivos y retorna en que subarbol se encuentra
		colour_balance_factor = self.__get_colour_balance_factor(node)

		if colour_balance_factor == "none":
			return node
		elif colour_balance_factor == "left":
			# verificar si el otro hijo es rojo
			if node.right is not None and node.right.colour == RBNode.RED:
				self.__spray_black_node(node)
			else: # caso en que el otro hijo es negro
				if node.left.left is not None and node.left.left.colour == RBNode.RED:
					node = self.__right_rotation(node)
				else:
					node.left = self.__left_rotation(node.left)
					node = self.__right_rotation(node)
			return node
		elif colour_balance_factor == "right":
			# verificar si el otro hijo es rojo
			if node.left is not None and node.left.colour == RBNode.RED:
				self.__spray_black_node(node)
			else: # caso en que el otro hijo es negro
				if node.right.right is not None and node.right.right.colour == RBNode.RED:
					node = self.__left_rotation(node)
				else:
					node.right = self.__right_rotation(node.right)
					node = self.__left_rotation(node)
			return node


	def _insert_node(self,root,node_type,value):
		# insercion simple del BST
		if self.root is None:
			new_node = super()._create_node(node_type,value)
			new_node.colour = RBNode.BLACK
			root = new_node
		elif not root:
			root = super()._create_node(node_type, value)
		else:
			new_node = super()._create_node(node_type, value)

			# insertar a la izquierda
			if new_node < root:
				root.left = self._insert_node(root.left, node_type, value)
			# insertar a la derecha
			else:
				root.right = self._insert_node(root.right, node_type, value)
			# balancear si el nodo es negro
			if root.colour == RBNode.BLACK: root = self.__balance_colour(root)


		return root

	def _exist(self, root, node):
		return super()._exist(root, node)

	def insert(self,value):
		self.root = self._insert_node(self.root,'RBNode',value)

	def search(self,value):
		node = super()._create_node('RBNode',value)
		return self._exist(self.root,node)

	def print_tree(self):
		self.__inorder(self.root)