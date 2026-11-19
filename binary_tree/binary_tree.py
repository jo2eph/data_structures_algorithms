"""
Implementation of a general Binary Tree in Python.
Note that this is not a Binary Search Tree (BST) implementation.
"""

class BTreeNode:
    """
    BTreeNode class represents a single node in a Binary Tree.
    Each node has a value, a left child, a right child, and a parent (except the root).
    The type of parent, left, and right is BTreeNode or None.
    """
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
    

    def __repr__(self):
        return f"BTreeNode(value={self.value})"
    

    def is_leaf(self):
        """
        Returns True if the node is a leaf node (has no children).
        False otherwise.
        """
        return self.left is None and self.right is None
    

    def has_children(self):
        """
        Returns True if the node has at least one child.
        False otherwise.
        """
        return self.left is not None or self.right is not None


    def set_parent(self, parent):
        """
        Sets the parent of the node.
        """
        self.parent = parent
    

    def set_left(self, left):
        """
        Sets the left child of the node.
        """
        self.left = left
    

    def set_right(self, right):
        """
        Sets the right child of the node.
        """
        self.right = right
    

    def set_children(self, left, right):
        """
        Sets both the children of the node.
        """
        self.left = left
        self.right = right
    

    def get_children(self):
        """
        Returns a tuple containing the left and right children of the node.
        """
        return (self.left, self.right)


class BinaryTree:
    """
    BinaryTree class represents a Binary Tree data structure.
    It supports basic operations such as:
    - insertion
    - deletion
    - searching
    - traversal (in-order, pre-order, post-order)
    """

    def __init__(self, root=None):
        self.root = root

    # ---------------------------------------------

    def insert(self, value):
        """
        Inserst a new node into the binary tree.
        """
        pass


    def delete(self, value):
        """
        Deletes a node from the binary tree.
        """
        pass


    def search(self, value):
        """
        Searches for a node in the binary tree.
        Returns the node if found, else returns None.
        """
        pass


    def traverse(self, order='in-order'):
        """
        Traverses the binary tree in the specified order.
        Default is in-order traversal.

        The order parameter must be one of the following:
        - 'in-order':

        - 'pre-order':
        
        - 'post-order':
        """
        if order == 'in-order':
            return self._in_order_traversal(self.root)
        elif order == 'pre-order':
            return self._pre_order_traversal(self.root)
        elif order == 'post-order':
            return self._post_order_traversal(self.root)
        else:
            raise ValueError("Invalid traversal order. Choose from 'in-order', 'pre-order', 'post-order'")
        
    # ---------------------------------------------
    
    def _in_order_traversal(self, node):
        """
        Traverses the binary tree via in-order traversal
        left -> root -> right
        Returns a list of node values in the order they were visited.
        """
        in_order_result = []

        if node is not None:
            in_order_result.extend(self._in_order_traversal(node.left))
            in_order_result.append(node.value)
            in_order_result.extend(self._in_order_traversal(node.right))

        return in_order_result


    def _pre_order_traversal(self, node):
        """
        Traverses the binary tree via pre-order traversal
        root -> left -> right
        Returns a list of node values in the order they were visited.
        """
        pre_order_result = []

        if node is not None:
            pre_order_result.append(node.value)
            pre_order_result.extend(self._pre_order_traversal(node.left))
            pre_order_result.extend(self._pre_order_traversal(node.right))

        return pre_order_result


    def _post_order_traversal(self, node):
        """
        Traverses the binary tree via post-order traversal
        left -> right -> root
        Returns a list of node values in the order they were visited.
        """
        post_order_result = []

        if node is not None:
            post_order_result.extend(self._post_order_traversal(node.left))
            post_order_result.extend(self._post_order_traversal(node.right))
            post_order_result.append(node.value)

        return post_order_result

