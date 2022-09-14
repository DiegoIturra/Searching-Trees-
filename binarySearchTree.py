import sys
from binaryTreeClass import BinaryTreeClass, Node, NodeFactory

sys.setrecursionlimit(10**6)

class BinarySearchTree(BinaryTreeClass):

    def __init__(self):
        self.root = None
        self.factory = NodeFactory()

    # Realiza un recorrido inorder del arbol
    def __inorder(self, root):
        if root is not None:
            self.__inorder(root.left)
            print(root)
            self.__inorder(root.right)

    # Crea un nodo en base al tipo de nodo
    def _create_node(self, node_type, value):
        return self.factory.get_node(node_type,value)

    # Inserta un nodo en el arbol
    def _insert_node(self, root, node_type, value):
        if not root:
            root = self._create_node(node_type, value)
        else:
            new_node = self._create_node(node_type, value)

            # insertar a la izquierda
            if new_node < root:
                root.left = self._insert_node(root.left, node_type, value)
            # insertar a la derecha
            else:
                root.right = self._insert_node(root.right, node_type, value)

        return root

    # Verifica que un nodo exista en el arbol
    def _exist(self, root, node):
        if not root:
            return False
        if root == node:
            return True
        if node < root:
            return self._exist(root.left, node)
        else:
            return self._exist(root.right, node)

    # metodos publicos
    def print_tree(self):
        self.__inorder(self.root)

    def insert(self, value):
        self.root = self._insert_node(self.root, 'Node', value)

    def search(self, value):
        node = self._create_node('Node', value)
        return self._exist(self.root, node)
