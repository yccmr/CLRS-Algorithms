# Implementation of BST
# Assume all keys are distinct

def is_bst(root):
    """ Return true if the binary tree rooted at `root` is a BST """
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    elif root.left is None and root.right is not None:
        if root.key < general_get_min(root.right):
            return is_bst(root.right)
    elif root.left is not None and root.right is None:
        if root.key > general_get_max(root.left):
            return is_bst(root.left)
    else:
        if root.key < general_get_min(root.right) and root.key > general_get_max(root.left):
            return is_bst(root.left) and is_bst(root.right)
    return False


def general_get_max(root):
    """ Find the max element in the binary tree rooted at `root` """
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root.key
    elif root.left is None and root.right is not None:
        return max(root.key, general_get_max(root.right))
    elif root.left is not None and root.right is None:
        return max(root.key, general_get_max(root.left))
    else:
        return max(root.key, general_get_max(root.left), general_get_max(root.right))


def general_get_min(root):
    """ Find the min element in the binary tree rooted at `root` """
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root.key
    elif root.left is None and root.right is not None:
        return min(root.key, general_get_max(root.right))
    elif root.left is not None and root.right is None:
        return min(root.key, general_get_max(root.left))
    else:
        return min(root.key, general_get_max(root.left), general_get_max(root.right))


class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def is_found(self, root, target):
        if root is None:
            return False
        elif root.key == target:
            return True
        elif root.key < target:
            return self.is_found(root.right, target)
        else:
            return self.is_found(root.left, target)

    def get_max(self, root):
        if root is None:
            return None
        if root.right is None:
            return root.key
        else:
            return self.get_max(root.right)

    def get_min(self, root):
        if root is None:
            return None
        if root.left is None:
            return root.key
        else:
            return self.get_min(root.left)

    def insert(self, root, new):
        """ Insert target into the BST (if it doesn't exist) s.t. the BST property is maintained """
        if self.is_found(root, new):
            return
        if root is None:
            self.root = BSTNode(new)
        else:
            if root.left is None and new < root.key:
                root.left = BSTNode(new)
            elif root.right is None and new > root.key:
                root.right = BSTNode(new)
            elif new < root.key:
                self.insert(root.left, new)
            elif new > root.key:
                self.insert(root.right, new)

    def delete(self, root, target):
        """ Delete target from the BST (if it exists) s.t. the BST property is maintained, and return the new root """
        if root is None or not self.is_found(root, target):
            return root
        else:
            if root.key < target:
                root.right = self.delete(root.right, target)
                return root
            elif root.key > target:
                root.left = self.delete(root.left, target)
                return root
            else:
                if root.left is None and root.right is None:     # no child
                    return None
                elif root.left is None and root.right is not None:     # one right child
                    return root.right
                elif root.left is not None and root.right is None:     # one left child
                    return root.left
                else:     # two children
                    left_max = self.get_max(root.left)
                    root.key = left_max
                    root.left = self.delete(root.left, left_max)
                    return root

    def inorder_string_repr(self, root):
        if self.is_empty():
            return "(empty)"
        else:
            if root is None:
                return ''
            else:
                return self.inorder_string_repr(root.left) + str(root.key) + self.inorder_string_repr(root.right)

    def __str__(self):     # should draw this as a tree...
        return self.inorder_string_repr(self.root)


