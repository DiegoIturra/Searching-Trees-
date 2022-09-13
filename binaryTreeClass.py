from abc import ABC, abstractmethod


class Node:

    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.value < other.value
        return False

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.value > other.value
        return False

    def __str__(self):
        return f"Node: {self.value}"


class AVLNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self._height = 0

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


class RBNode(AVLNode):
    RED = 1
    BLACK = 0

    def __init__(self, value):
        super().__init__(value)
        self.colour = RBNode.BLACK
        self.parent = None

    def __str__(self):
        colour = "Black" if self.colour == 0 else "Red"
        return f"(Node: {self.value},Colour: {colour})"


class NodeFactory:

	def get_node(self,node_type,value):
		if node_type == 'Node':
			return Node(value)
		elif node_type == 'AVLNode':
			return AVLNode(value)
		elif node_type == 'RBNode':
			return RBNode(value)
		return None


class BinaryTreeClass(ABC):

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def search(self, value):
        pass
