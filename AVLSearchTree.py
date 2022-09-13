from binarySearchTree import BinarySearchTree


class AVLSearchTree(BinarySearchTree):

    def __init__(self):
        super().__init__()

    # Actualiza la altura de un nodo referenciado, en base al maximo entre el sub arbol izquierdo y derecho mas 1
    def __update_height(self, node):
        node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1

    # Retorna el valor de la alura asociado al nodo referenciado
    def __get_height(self, node):
        return -1 if not node else node.height

    # Retorna el factor de balance de un nodo referenciado
    def __get_balance_factor(self, node):
        return self.__get_height(node.right) - self.__get_height(node.left)

    # Rotacion izquierda
    def __left_rotation(self, node):
        aux_node = node.right
        node.right = aux_node.left
        aux_node.left = node

        self.__update_height(node)
        self.__update_height(aux_node)

        return aux_node

    # Rotacion derecha
    def __right_rotation(self, node):
        aux_node = node.left
        node.left = aux_node.right
        aux_node.right = node

        self.__update_height(node)
        self.__update_height(aux_node)

        return aux_node

    # Retorna un nodo balanceado
    def __balance(self, node):
        balance_factor = self.__get_balance_factor(node)

        # Arbol cargado hacia la izquierda
        if balance_factor < -1:
            if self.__get_balance_factor(node.left) <= 0:
                node = self.__right_rotation(node)
            else:
                node.left = self.__left_rotation(node.left)
                node = self.__right_rotation(node)

        # Arbol cargado hacia la derecha
        if balance_factor > 1:
            if self.__get_balance_factor(node.right) >= 0:
                node = self.__left_rotation(node)
            else:
                node.right = self.__right_rotation(node.right)
                node = self.__left_rotation(node)

        return node

    def __inorder(self, root):
        if root is not None:
            self.__inorder(root.left)
            print(f"{root} / heigth : {root.height} / balance_factor : {self.__get_balance_factor(root)}")
            self.__inorder(root.right)

    def _insert_node(self, root, node_type, value):
        # LLama a la insercion del BST
        root = super()._insert_node(root, node_type, value)

        # Actualiza la altura
        self.__update_height(root)

        # Retorna un nodo balanceado
        return self.__balance(root)

    def _exist(self, root, node):
        return super()._exist(root, node)

    # Metodos publicos
    def print_tree(self):
        self.__inorder(self.root)

    def insert(self, value):
        self.root = self._insert_node(self.root, 'AVLNode', value)

    def search(self, value):
        node = super()._create_node('AVLNode', value)
        return self._exist(self.root, node)
