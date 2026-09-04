"""
Tests for linked list.
"""

from linked_list import LinkedList

import pytest


def test_linked_list_initialization():
    ll = LinkedList()
    assert ll.head is None


def test_linked_list_repr_empty():
    ll = LinkedList()
    assert repr(ll) == "HEAD: NULL"


def test_linked_list_len_empty():
    ll = LinkedList()
    assert len(ll) == 0


def test_linked_list_append():
    # This linked list should look like HEAD: 1 -> 2 -> 3 -> NULL
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert ll.to_list() == [1, 2, 3]


def test_linked_list_insert():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.insert(1, 2)  # Insert 2 at index 1

    assert ll.to_list() == [1, 2, 3]


def test_linked_list_insert_at_head():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.insert(0, 1)  # Insert 1 at index 0 (head)

    assert ll.to_list() == [1, 2, 3]


def test_linked_list_insert_at_end():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert(5, 3)  # Insert 3 at index 5 (end)

    assert ll.to_list() == [1, 2, 3]