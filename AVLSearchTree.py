from binaryTreeClass import Node, BinaryTreeClass


class AVLSearchTree(BinaryTreeClass):

    def __init__(self):
        self.root = None

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

    def __balance(self,node):
    	balance_factor = self.__get_balance_factor(node)

    	
    	#Arbol cargado hacia la izquierda
    	if balance_factor < -1:
    		if self.__get_balance_factor(node.left) <= 0:
    			node = self.__right_rotation(node)
    		else:
    			node.left = self.__left_rotation(node.left)
    			node = self.__right_rotation(node)

    	#Arbol cargado hacia la derecha
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


    def __create_node(self, value):
        return Node(value)


    def __insert_node(self, root, value):
        if not root:
            return self.__create_node(value)
        else:
            new_node = self.__create_node(value)
            # insertar a la izquierda
            if new_node < root:
                root.left = self.__insert_node(root.left, value)
            # insertar a la derecha
            elif new_node > root:
                root.right = self.__insert_node(root.right, value)

        # Actualiza la altura
        self.__update_height(root)

        return self.__balance(root)


    def __exist(self, root, node):
        if not root:
            return False
        if root == node:
            return True
        if node < root:
            return self.__exist(root.left, node)
        else:
            return self.__exist(root.right, node)


    # Metodos publicos
    def print_tree(self):
        self.__inorder(self.root)

    def insert(self, value):
        self.root = self.__insert_node(self.root, value)

    def search(self, value):
        node = self.__create_node(value)
        return self.__exist(self.root, node)

