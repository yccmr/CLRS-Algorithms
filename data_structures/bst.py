# Implementation of BST
# Assume all keys are distinct

def is_bst(root):
    """ Return true if the binary tree rooted at `root` is a BST """
    if root is None:
        return True
    if root.get_left() is None and root.get_right() is None:
        return True
    elif root.get_left() is None and root.get_right() is not None:
        if root.get_data() < general_get_min(root.get_right()):
            return is_bst(root.get_right())
    elif root.get_left() is not None and root.get_right() is None:
        if root.get_data() > general_get_max(root.get_left()):
            return is_bst(root.get_left())
    else:
        if root.get_data() < general_get_min(root.get_right()) and root.get_data() > general_get_max(root.get_left()):
            return is_bst(root.get_left()) and is_bst(root.get_right())
    return False


def general_get_max(root):
    """ Find the max element in the binary tree rooted at `root` """
    if root is None:
        return None
    if root.get_left() is None and root.get_right() is None:
        return root.get_data()
    elif root.get_left() is None and root.get_right() is not None:
        return max(root.get_data(), general_get_max(root.get_right()))
    elif root.get_left() is not None and root.get_right() is None:
        return max(root.get_data(), general_get_max(root.get_left()))
    else:
        return max(root.get_data(), general_get_max(root.get_left()), general_get_max(root.get_right()))


def general_get_min(root):
    """ Find the min element in the binary tree rooted at `root` """
    if root is None:
        return None
    if root.get_left() is None and root.get_right() is None:
        return root.get_data()
    elif root.get_left() is None and root.get_right() is not None:
        return min(root.get_data(), general_get_max(root.get_right()))
    elif root.get_left() is not None and root.get_right() is None:
        return min(root.get_data(), general_get_max(root.get_left()))
    else:
        return min(root.get_data(), general_get_max(root.get_left()), general_get_max(root.get_right()))


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

    def get_root(self):
        return self.__root

    def set_root(self, new_root):
        self.__root = new_root

    def is_empty(self):
        return self.__root is None

    def is_found(self, root, target):
        if root is None:
            return False
        elif root.get_data() == target:
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

    def insert(self, root, new):
        """ Insert target into the BST (if it doesn't exist) s.t. the BST property is maintained """
        if self.is_found(root, new):
            return
        if root is None:
            self.__root = BSTNode(new)
        else:
            if root.get_left() is None and new < root.get_data():
                root.set_left(BSTNode(new))
            elif root.get_right() is None and new > root.get_data():
                root.set_right(BSTNode(new))
            elif new < root.get_data():
                self.insert(root.get_left(), new)
            elif new > root.get_data():
                self.insert(root.get_right(), new)

    def delete(self, root, target):
        """ Delete target from the BST (if it exists) s.t. the BST property is maintained, and return the new root """
        if root is None or not self.is_found(root, target):
            return root
        else:
            if root.get_data() < target:
                root.set_right(self.delete(root.get_right(), target))
                return root
            elif root.get_data() > target:
                root.set_left(self.delete(root.get_left(), target))
                return root
            else:
                if root.get_left() is None and root.get_right() is None:     # no child
                    return None
                elif root.get_left() is None and root.get_right() is not None:     # one right child
                    return root.get_right()
                elif root.get_left() is not None and root.get_right() is None:     # one left child
                    return root.get_left()
                else:     # two children
                    left_max = self.get_max(root.get_left())
                    root.set_data(left_max)
                    root.set_left(self.delete(root.get_left(), left_max))
                    return root

    def inorder_string_repr(self, root):
        if self.is_empty():
            return "(empty)"
        else:
            if root is None:
                return ''
            else:
                return self.inorder_string_repr(root.get_left()) + str(root.get_data()) + self.inorder_string_repr(root.get_right())

    def __str__(self):     # should draw this as a tree...
        return self.inorder_string_repr(self.__root)


