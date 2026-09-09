"""
Tests for binary tree
"""

from binary_tree import *

def test_binary_tree_initialization():
    bt = BinaryTree()
    assert bt.root is None


def test_binary_tree_traversals():
    # Create a binary tree
    #     1
    #    /  \
    #   2    3
    #  / \  / \
    # 4  5  6  7
    root = BTreeNode(1)

    left = BTreeNode(2)
    right = BTreeNode(3)
    root.set_children(left, right)

    left_left = BTreeNode(4)
    left_right = BTreeNode(5)
    left.set_children(left_left, left_right)

    right_left = BTreeNode(6)
    right_right = BTreeNode(7)
    right.set_children(right_left, right_right)

    bt = BinaryTree(root)

    # In-order traversal should return [4, 2, 5, 1, 6, 3, 7]
    assert bt.traverse(order='in-order') == [4, 2, 5, 1, 6, 3, 7]

    # Pre-order traversal should return
    assert bt.traverse(order='pre-order') == [1, 2, 4, 5, 3, 6, 7]