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

    def is_found(self, target):
        pass

    def get_max(self):
        pass

    def get_min(self):
        pass

    def insert(self, target):
        """ Insert target into the BST (if it doesn't exist) s.t. the BST property is maintained """
        pass

    def delete(self, target):
        """ Delete target from the BST (if it exists) s.t. the BST property is maintained """
        pass

    def __str__(self):
        pass


