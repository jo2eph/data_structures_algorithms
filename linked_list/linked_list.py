"""
Implementation of a singly linked list in Python.
"""

from collections.abc import Iterable


class Node:
    """
    Node class represents a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    LinkedList class represents a singly linked list data structure.

    This linked list implementation supports basic operations such as:
    - .append(data) 
        Appending a new node to the end of the list (O(n))
    - .insert(index, data)
        Inserting at a specific index (O(n))
    - .delete_by_value(value)
        Deleting a node by value (O(n))
    - .delete_by_index(index)
        Deleting a node by index (O(n))
    - .reverse()
        Reversing the linked list
    - .search(value)
        Searching for a node by value (O(n))
    - .length
        Getting the length
    - .to_list()
        Converting linked list to a Python list (O(n))
    - .from_list(lst)
        Converting Python list to linked list (O(n))

    Example:
    --------

    >>> my_linked_list = LinkedList()
    >>> my_linked_list.append(1)
    >>> my_linked_list.append(2)
    >>> my_linked_list.append(3)
    >>> print(my_linked_list)
    HEAD: 1 -> 2 -> 3 -> NULL
    """

    # Constructor 
    def __init__(self, lst=None):
        self.head = None
        self.length = 0

        # If a list is provided, initialize the linked list with its elements
        if lst is not None:
            self.from_list(lst)
            self.length = len(lst)
    
    
    # String representation
    def __repr__(self):
        str_repr = "HEAD: "
        current = self.head

        while current:
            str_repr += f"{current.data} -> "
            current = current.next

        str_repr += "NULL"
        return str_repr


    # Length of the linked list
    def __len__(self):
        return self.length


    def append(self, data) -> None:
        """
        Insert a new node with the given data to the end of the linked list.
        """
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.length += 1

    
    def insert(self, index, data) -> None:
        """
        Insert a new node at a specified index.
        If the index is greater than the length of the list, the new node will be appended to the end.
        If the index is less than or equal to 0, the new node will be the new head of the list.
        """

        new_node = Node(data)

        # Handle edge cases for index
        if index <= 0:
            new_node.next = self.head
            self.head = new_node

            self.length += 1
        elif index >= self.length:
            self.append(data)
        
        # Insert in the middle of the list
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

            self.length += 1


    def to_list(self) -> list:
        """
        Convert the linked list to a Python list.
        The head node becomes the first element (index 0) of the list.
        """

        list_representation = []

        current = self.head

        while current:
            list_representation.append(current.data)
            current = current.next

        return list_representation
    

    def from_list(self, lst) -> None:
        """
        Convert a Python list to a linked list, where the first element of the list becomes the head.
        """

        for item in lst:
            self.append(item)
