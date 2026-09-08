"""
Imlementation of a dynamic array data structure in Python.
"""

class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
    

    def __len__(self):
        return self.size
    

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]