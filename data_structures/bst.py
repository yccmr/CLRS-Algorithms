# Implementation of BST

def is_BST(root):
    """ Return true if the binary tree rooted at `root` is a BST """
    pass


def general_get_max(root):
    """ Find the max element in the binary tree rooted at `root` """
    pass


def general_get_min(root):
    """ Find the min element in the binary tree rooted at `root` """
    pass


class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data

    def get_left(self):
        return self.__left

    def set_left(self, new_left):
        self.__left = new_left

    def get_right(self):
        return self.__right

    def set_right(self, new_right):
        self.__right = new_right


class BST:
    def __init__(self, root=None):
        self.__root = root

    def is_found(self, root, target):
        if root is None:
            return False
        else:
            if root.get_data() == target:
                return True
            elif root.get_data() < target:
                return self.is_found(root.get_right(), target)
            else:
                return self.is_found(root.get_left(), target)

    def get_max(self, root):
        if root is None:
            return None
        if root.get_right() is None:
            return root.get_data()
        else:
            return self.get_max(root.get_right())

    def get_min(self, root):
        if root is None:
            return None
        if root.get_left() is None:
            return root.get_data()
        else:
            return self.get_min(root.get_left())

    def insert(self, root, target):
        """ Insert target into the BST (if it doesn't exist) s.t. the BST property is maintained """
        pass

    def delete(self, root, target):
        """ Delete target from the BST (if it exists) s.t. the BST property is maintained """
        pass

    def __str__(self):
        pass


